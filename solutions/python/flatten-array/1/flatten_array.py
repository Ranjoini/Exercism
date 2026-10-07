def flatten(iterable):
    def extraction_engine(nested_data):
        for item in nested_data:
            if item is None:
                continue
            if isinstance(item, (list, tuple)):
                yield from extraction_engine(item)
            else:
                yield item

    return list(extraction_engine(iterable))
