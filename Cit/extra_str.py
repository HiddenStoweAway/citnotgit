def is_alphebetic(src) -> bool:
    return (not(src.upper() == src.lower()) or src in './\\:')

def is_numeric(src) -> bool:
    numbers = '0123456789'
    return src in numbers