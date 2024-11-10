"""Alchemy."""
from typing import Optional


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str):
        """Alchemical element constructor.

        :param name: element has one name.
        """
        self.name = name

    def __repr__(self) -> str:
        """Alchemical element representation.

        :return: string: So that you can read, dummy.
        """
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.elements_list = []
        self.elements_dict = {}

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in
        TypeError exception.

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement) is False:
            raise TypeError("Element must be an instance of Object 'AlchemicalElement'")
        else:
            self.elements_list.append(element)
        return self.elements_list

    def pop(self, element_name: str) -> Optional[AlchemicalElement]:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        global x
        i = len(self.elements_list) - 1
        while i >= 0:
            for element in reversed(self.elements_list):
                i -= 1
                if element.name == element_name:
                    self.elements_list.remove(element)
                    return element

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        result = []
        if len(self.elements_list) > 0:
            for element in self.elements_list:
                result.append(element)
            self.elements_list.clear()
            return result
        else:
            return self.elements_list

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        for element in self.elements_list:
            if element.name not in self.elements_dict.keys():
                self.elements_dict[element.name] = 1
            else:
                if element.name in self.elements_dict.keys():
                    self.elements_dict[element.name] += 1

        result_content_string = "Content:\n"
        result_elements = ''

        if len(sorted(self.elements_dict.keys())) == 0:
            result_elements += " Empty."

        for k, v in sorted(self.elements_dict.items()):
            result_elements += (" * " + str(k) + " x " + str(v)) + '\n'

        without_nl = (result_elements.rstrip('\n'))
        return result_content_string + without_nl


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        Add whatever you need to make this class function.
        """
        self.recipes_book = {}

    def __repr__(self):
        """
        Recipe representation.

        :return:
        """

    def get_component_names(self, product_name: str) -> tuple[str, str] | None:
        """
        Take in product name and returns the names of two components, that are necessary for that product.

        If there are no recipes that would produce the product return None. Order of the components does not matter.
        It can be assumed that for one product there is only one recipe.

        :param product_name:
        :return:
        """
        result = ()
        for k, v in self.recipes_book.items():
            if product_name == k:
                result = tuple(set(v))
        if len(result) > 0:
            return tuple(result)
        else:
            return None

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        if first_component_name == second_component_name or first_component_name == product_name:
            raise DuplicateRecipeNamesException
        if product_name == first_component_name or product_name == second_component_name:
            raise DuplicateRecipeNamesException

        components = (first_component_name, second_component_name)

        for v in self.recipes_book.values():
            if set(components) == set(v):
                raise RecipeOverlapException

        self.recipes_book[product_name] = {first_component_name, second_component_name}

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str or None:
        """
        Return the name of the product for the two components.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).
        If there are no combinations for the two components, return None.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
            recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
            recipes.get_product_name('Fire', 'Water')  # ->  None
            recipes.add_recipe('Water', 'Fire', 'Steam')
            recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        components = (first_component_name, second_component_name)

        for k, v in self.recipes_book.items():
            if set(components) == set(v):
                result = k
                return result
        else:
            return None


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""

    pass


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""

    pass


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Cauldron class."""
        super().__init__()
        self.recipes = recipes

    def combine(self) -> bool:
        """Combine two elements."""
        pass

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            cauldron = Cauldron(recipes)
            cauldron.add(AlchemicalElement('Water'))
            cauldron.add(AlchemicalElement('Wind'))
            cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        super().add(element)

        self.combine()


class Catalyst(AlchemicalElement):
    """Catalyst class."""

    def __init__(self, name: str, uses: int):
        """
        Initialize the Catalyst class.

        :param name: The name of the Catalyst.
        :param uses: The number of uses the Catalyst has.
        """
        super().__init__(name)
        self.uses = uses

    def __repr__(self) -> str:
        """
        Representation of the Catalyst class.

        Example:
            catalyst = Catalyst("Philosophers' stone", 3)
            print(catalyst) # -> <C: Philosophers' stone (3)>

        :return: String representation of the Catalyst.
        """
        return f"<C: {self.name} ({self.uses})>"


class Purifier(AlchemicalStorage):
    """
    Purifier class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """Initialize the Purifier class."""
        super().__init__()
        self.recipes = recipes

    def split(self):
        """
        Split helper method.

        :return:
        """
        pass

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can be split into anything.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            purifier = Purifier(recipes)
            purifier.add(AlchemicalElement('Ice'))
            purifier.extract() # -> [<AE: Water>, <AE: Wind>]   or  [<AE: Wind>, <AE: Water>]

        :param element: Input object to add to storage.
        """
        super().add(element)
        for ae in self.elements_list:
            result = self.recipes.get_component_names(ae.name)
            if result is None:
                continue
            else:
                self.pop(ae.name)
                for one_ae in result:
                    super().add(AlchemicalElement(one_ae))


if __name__ == '__main__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Fire', 'Water', 'Steam')
    recipes.add_recipe('Fire', 'Earth', 'Iron')
    recipes.add_recipe('Water', 'Iron', 'Rust')
    recipes.add_recipe('Water', 'Wind', 'Ice')

    # print(recipes.get_component_names('Iron'))  # -> ('Fire', 'Earth')

    # catalyst = Catalyst("Philosophers' stone", 5)
    # print(catalyst)  # -> <C: Philosophers' stone (5)>

    purifier = Purifier(recipes)
    purifier.add(AlchemicalElement('Ice'))
    print(purifier.extract())  # -> [<AE: Water>, <AE: Wind>]   or  [<AE: Wind>, <AE: Water>]
    philosophers_stone = Catalyst("Philosophers' stone", 0)
    philosophers_stone1 = Catalyst("Philosophers' stone", 1)

    recipes = AlchemicalRecipes()
    recipes.add_recipe("Philosophers' stone", 'Mercury', 'Gold')
    # recipes.add_recipe("Philosophers' stone", "Philosophers' stone", '')

    recipes.add_recipe("Fire", 'Earth', 'Iron')

    cauldron = Cauldron(recipes)
    cauldron.add(philosophers_stone)
    # cauldron.add(philosophers_stone1)
    cauldron.add(AlchemicalElement('Mercury'))
    cauldron.add(philosophers_stone1)

    print(cauldron.extract())  # -> [<C: Philosophers' stone (1)>, <AE: Gold>]

    # cauldron.add(philosophers_stone)
    # cauldron.add(AlchemicalElement('Mercury'))
    # print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Gold>]

    # cauldron.add(philosophers_stone)
    # cauldron.add(AlchemicalElement('Mercury'))
    # print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Mercury>]

    # purifier = Purifier(recipes)
    # purifier.add(AlchemicalElement('Iron'))
    # print(purifier.extract())  # -> [<AE: Fire>, <AE: Earth>]    or      [<AE: Earth>, <AE: Fire>]


if __name__ == '__main2__':
    recipes = AlchemicalRecipes()
    recipes.add_recipe('Fire', 'Water', 'Steam')
    recipes.add_recipe('Fire', 'Earth', 'Iron')
    recipes.add_recipe('Water', 'Iron', 'Rust')

    print(recipes.get_product_name('Water', 'Fire'))  # -> 'Steam'

    # recipes.add_recipe('Water', 'Wind', 'Ice')
    # print(recipes.get_product_name('Water', 'Wind'))  # ->  'Ice'
    # print(recipes.get_product_name('Wind', 'Water'))  # ->  'Ice'
    # print(recipes.get_product_name('Fire', 'Water'))  # ->  None
    # recipes.add_recipe('Water', 'Fire', 'Steam')  # -> None
    # print(recipes.get_product_name('Fire', 'Water'))  # ->  'Steam'

    # try:
    # recipes.add_recipe('Fire', 'Something else', 'Fire')
    # print('Did not raise, not working as intended.')

    # except DuplicateRecipeNamesException:
    # print('Raised DuplicateRecipeNamesException, working as intended!')

    # try:
    # recipes.add_recipe('Fire', 'Earth', 'Gold')
    # print('Did not raise, not working as intended.')

    # except RecipeOverlapException:
    # print('Raised RecipeOverlapException, working as intended!')

    # print("--------------")
    cauldron = Cauldron(recipes)
    # print(cauldron.elements_list)
    # print()
    # cauldron.add(AlchemicalElement('Mud'))
    # cauldron.add(AlchemicalElement('Fire'))
    # cauldron.add(AlchemicalElement('Fire'))
    # cauldron.add(AlchemicalElement('Water'))

    # cauldron.add(AlchemicalElement('Mud'))
    # cauldron.add(AlchemicalElement('Earth'))
    # cauldron.add(AlchemicalElement('Water'))
    # cauldron.add(AlchemicalElement('Fire'))
    # print('...........................')
    # print(cauldron.elements_list)   # -> <AE: Water>, <AE: Iron>
    # exit()

    # print(cauldron.extract())  # -> [<AE: Earth>, <AE: Steam>]

    # cauldron.add(AlchemicalElement('Earth'))
    # cauldron.add(AlchemicalElement('Earth'))
    # cauldron.add(AlchemicalElement('Earth'))
    # cauldron.add(AlchemicalElement('Fire'))
    # cauldron.add(AlchemicalElement('Fire'))
    # cauldron.add(AlchemicalElement('Water'))

    # print(cauldron.extract())  # -> [<AE: Earth>, <AE: Iron>, <AE: Rust>]

    # recipes = AlchemicalRecipes()
    # print(recipes.add_recipe('Water', 'Wind', 'Ice'))
    # purifier = Purifier(recipes)
    # print(purifier.add(AlchemicalElement('Ice')))
    # print(purifier.extract())  # -> [<AE: Water>, <AE: Wind>]   or  [<AE: Wind>, <AE: Water>]
