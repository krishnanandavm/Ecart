from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk = []
    i = 0
    for x in list_data:
        chunk.append(x)
        i += 1
        if i == chunk_size:
            yield chunk
            chunk = []
            i = 0  # Reset the counter after yielding a chunk
    if chunk:  # Don't forget to yield the last chunk if it's not empty
        yield chunk
