def combine(self) -> bool:
    """Combine two elements."""
    pass
    """
    for first_element in reversed(self.elements_list):
        if isinstance(first_element, Catalyst):
            if first_element.uses == 0:
                continue
        for second_element in reversed(self.elements_list):
            if isinstance(second_element, Catalyst):
                if second_element.uses == 0:
                    continue
            if isinstance(second_element, Catalyst) and isinstance(first_element, Catalyst):
                if first_element != second_element:
                    if second_element.uses > 0 and first_element.uses > 0:
                        second_element.uses -= 1
                        first_element.uses -= 1
                else:
                    continue
            result = self.recipes.get_product_name(first_element.name, second_element.name)
            if result is not None:
                if isinstance(first_element, Catalyst):
                    if first_element.uses == 0:
                        continue
                    if first_element.uses > 0:
                        first_element.uses -= 1
                else:
                    self.pop(first_element.name)
                if isinstance(second_element, Catalyst):
                    if second_element.uses == 0:
                        continue
                    if second_element.uses > 0:
                        second_element.uses -= 1
                else:
                    self.pop(second_element.name)
                super(Cauldron, self).add(AlchemicalElement(result))
                return True
    return False
    """