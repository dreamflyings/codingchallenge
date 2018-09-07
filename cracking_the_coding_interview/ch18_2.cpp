// ch18.1: write a method to shuffle a deck of cards

#include <iostream>
#include <vector>
#include <stdlib.h>
#include <time.h>

#include <gtest/gtest.h>

using namespace std;

void shuffle_deck(vector<int> &deck) {
  for (unsigned i=0; i<deck.size(); i++) {
    int which = rand() % deck.size();
    int swap = deck[which];
    deck[i] = deck[which];
    deck[which] = swap;
  }
}

TEST(ch18_1, shuffle) {
  srand(time(NULL)); // randomize seed

  // initialize deck
  vector<int> deck = { };
  deck.resize(52);
  for (unsigned i=0; i<52; i++)
    deck[i] = i;

//    for (unsigned i=0; i<52; i++)
//        cout << deck[i] << " ";
//    cout << endl;

  // shuffle the deck
  shuffle_deck(deck);

  // visual inspection only ...
//    for (unsigned i=0; i<52; i++)
//        cout << deck[i] << " ";
//    cout << endl;
}
