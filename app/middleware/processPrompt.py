"""
Process prompts
"""
import json

from app.middleware.helper import execute_llm, remove_html_tags


def prepare_prompt_per_product(data):
    all_prompts = []
    spec_prompts = []
    for product in data:
        product_info = ""
        prompt_default = "given description below, can you find more info about this product? " \
                         "just show extra info that are not present in the description.\n description:"
        if 'taxonomy' in product:
            for taxonomy in product['taxonomy'].values():
                product_info += f' {taxonomy.lower()}'
        if 'description' in product:
            # Description has duplicates values with product_details,
            # and just makes the call longer and less accurate.
            if len(product['description']) <= 1000:
                product_info = remove_html_tags(product['description']).lower()
        if 'product_details' in product:
            for key, value in product['product_details'].items():
                product_info += f", {key.lower()} is {value}"

        prompt_default += f' {product_info}'
        all_prompts.append(prompt_default)

        if 'priceUSD' in product and product['priceUSD'] != 0:
            product_info += f"price is {product['priceUSD']}"
        price_weight_default_prompt = "given description below, find and only indicate " \
                                      "the price and weight of the product. if weight is varied by size, " \
                                      "indicate all. FORCE response format to: price: <price>, weight: <weight> " \
                                      "without any additional text. If any value not found, just put NA." \
                                      " \n description:"
        price_weight_default_prompt += f' {product_info}'
        spec_prompts.append(price_weight_default_prompt)

    return all_prompts, spec_prompts


def prompt_response(json_string) -> str:
    product_data = json.loads(json_string)
    all_prompts, spec_prompts = prepare_prompt_per_product(product_data)

    print(f"Loaded {len(all_prompts)} prompts for spec and augmented data. Starting data augmentation...")
    augmented_data = [execute_llm(prompt) for prompt in all_prompts]

    print(f"Augmented data has been generated. Starting on Specs now...")
    spec_data = [execute_llm(spec_prompt) for spec_prompt in spec_prompts]

    print(f"Spec data has been generated. Updating the file...")
    for i, product in enumerate(product_data):
        if augmented_data and augmented_data[i] and "augmented_data" not in product:
            product['augmented_data'] = augmented_data[i]
        if spec_data and 'price:' in spec_data[i] and ', weight' in spec_data[i]:
            price = spec_data[i].split('price:')[1].split(', weight')[0].strip()
            weight = spec_data[i].split(', weight:')[1].strip()
            if product["priceUSD"] == 0 and price != 'na':
                product['price'] = price
            if weight != 'na':
                product['weight'] = weight

    return f" Here are the product details: {json.dumps(product_data, indent=4)}"


