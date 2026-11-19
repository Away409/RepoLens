#include "greeter.hpp"
#include <iostream>

int main() {
    std::cout << demo::Greeter{}.message() << '\n';
}
