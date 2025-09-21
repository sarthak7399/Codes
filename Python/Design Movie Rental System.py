# https://leetcode.com/problems/design-movie-rental-system/

# Example 1:
# Input
# ["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
# [[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
# Output
# [null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]
# Explanation
# MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
# movieRentingSystem.search(1);  // return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
# movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
# movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
# movieRentingSystem.report();   // return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
# movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
# movieRentingSystem.search(2);  // return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # Maps (shop, movie) -> price for quick lookup
        self.available = {}

        # Maps movie -> sorted list of (price, shop) pairs
        # Helps in searching cheapest shops for a given movie
        self.movie_shops = {}

        # Keeps track of currently rented movies as (shop, movie) pairs
        self.rented = set()

        # Load initial entries
        for shop, movie, price in entries:
            self.available[(shop, movie)] = price

            # Add entry to movie-specific list
            if movie not in self.movie_shops:
                self.movie_shops[movie] = []
            self.movie_shops[movie].append((price, shop))

        # Sort shops for each movie by price (then shop ID as tie-breaker)
        for movie in self.movie_shops:
            self.movie_shops[movie].sort()

    def search(self, movie: int) -> List[int]:
        """
        Return up to 5 shops (by ascending price, then shop ID) 
        where the given movie is available (not rented).
        """
        result = []
        for price, shop in self.movie_shops.get(movie, []):
            if (shop, movie) not in self.rented:  # only consider available ones
                result.append(shop)
            if len(result) == 5:  # limit to 5 shops
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        """
        Mark a movie as rented from a given shop.
        """
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        """
        Mark a movie as returned (remove from rented set).
        """
        self.rented.discard((shop, movie))

    def report(self) -> List[List[int]]:
        """
        Return up to 5 rented movies sorted by:
          - price ascending
          - shop ID ascending
          - movie ID ascending
        Each entry is [shop, movie].
        """
        rented_list = []
        for shop, movie in self.rented:
            price = self.available[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()  # sort by (price, shop, movie)
        return [[shop, movie] for price, shop, movie in rented_list[:5]]
