#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

// Base class for all units
class Unit {
public:
    string name;
    int health;
    int damage;

    Unit(string n, int h, int d) : name(n), health(h), damage(d) {}

    void attack(Unit& target) {
        cout << name << " attacks " << target.name << " for " << damage << " damage!" << endl;
        target.health -= damage;
        if (target.health <= 0) {
            cout << target.name << " has been defeated!" << endl;
        }
    }
};

// Derived classes for different troop types
class Barbarian : public Unit {
public:
    Barbarian() : Unit("Barbarian", 30, 5) {}
};

class Archer : public Unit {
public:
    Archer() : Unit("Archer", 20, 4) {}
};

// Game class to manage resources, troops, and battles
class Game {
private:
    int gold;
    int elixir;
    vector<Unit*> troops;

public:
    Game() : gold(100), elixir(100) {}

    void showResources() {
        cout << "Gold: " << gold << ", Elixir: " << elixir << endl;
    }

    void trainTroop(string troopType) {
        if (troopType == "Barbarian") {
            if (gold >= 10 && elixir >= 5) {
                troops.push_back(new Barbarian());
                gold -= 10;
                elixir -= 5;
                cout << "Trained a Barbarian!" << endl;
            } else {
                cout << "Not enough resources to train a Barbarian!" << endl;
            }
        } else if (troopType == "Archer") {
            if (gold >= 15 && elixir >= 8) {
                troops.push_back(new Archer());
                gold -= 15;
                elixir -= 8;
                cout << "Trained an Archer!" << endl;
            } else {
                cout << "Not enough resources to train an Archer!" << endl;
            }
        } else {
            cout << "Unknown troop type!" << endl;
        }
    }

    void attackEnemyBase() {
        if (troops.empty()) {
            cout << "You have no troops to attack!" << endl;
            return;
        }

        cout << "Attacking enemy base!" << endl;
        int enemyHealth = 100;

        for (Unit* troop : troops) {
            troop->attack(*new Unit("Enemy", enemyHealth, 0));
            enemyHealth -= troop->damage;
            if (enemyHealth <= 0) {
                cout << "You defeated the enemy base!" << endl;
                return;
            }
        }
        cout << "The enemy base has " << enemyHealth << " health left." << endl;
    }

    ~Game() {
        for (Unit* troop : troops) {
            delete troop;
        }
    }
};

int main() {
    Game game;
    string command;

    cout << "Welcome to Clash of Clans!" << endl;

    while (true) {
        cout << "\nAvailable commands: show resources, train barbarian, train archer, attack, exit" << endl;
        cout << "Enter command: ";
        getline(cin, command);

        if (command == "show resources") {
            game.showResources();
        } else if (command == "train barbarian") {
            game.trainTroop("Barbarian");
        } else if (command == "train archer") {
            game.trainTroop("Archer");
        } else if (command == "attack") {
            game.attackEnemyBase();
        } else if (command == "exit") {
            cout << "Exiting game..." << endl;
            break;
        } else {
            cout << "Unknown command!" << endl;
        }
    }

    return 0;
}
