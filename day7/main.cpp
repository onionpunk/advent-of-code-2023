#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

const int NUMBER_BASE = 14;
const int TOTAL_CARDS_ON_HAND = 5;

map<char, int> CARD_MAP{
		{'1', 1},
		{'2', 2},
		{'3', 3},
		{'4', 4},
		{'5', 5},
		{'6', 6},
		{'7', 7},
		{'8', 8},
		{'9', 9},
		{'T', 10},
		{'J', 11},
		{'Q', 12},
		{'K', 13},
		{'A', 14},
};

map<char, int> CARD_MAP2{
		{'1', 1},
		{'2', 2},
		{'3', 3},
		{'4', 4},
		{'5', 5},
		{'6', 6},
		{'7', 7},
		{'8', 8},
		{'9', 9},
		{'T', 10},
		{'J', 1}, // in part 2 this is Joker card and is as weak as 1
		{'Q', 12},
		{'K', 13},
		{'A', 14},
};

enum HandKind
{
	HIGH_CARD = 0,
	ONE_PAIR = 1,
	TWO_PAIR = 2,
	THREE_OF_A_KIND = 3,
	FULL_HOUSE = 4,
	FOUR_OF_A_KIND = 5,
	FIVE_OF_A_KIND = 6,
};

struct CardHand
{
private:
	string _cards;
	vector<char> _handKindDistinctCard;
	vector<int> _handKindCardCount;
	map<char, int> _cardCount;
	string _handKindString = "";

	void evaluateRule1()
	{
		if (this->_cardCount.size() == 1)
		{
			this->kind = FIVE_OF_A_KIND;
		}
		else if (this->_cardCount.size() == 2)
		{
			if (_handKindString == "14")
			{
				this->kind = FOUR_OF_A_KIND;
			}
			else if (_handKindString == "23")
			{
				this->kind = FULL_HOUSE;
			}
		}
		else if (this->_cardCount.size() == 3)
		{
			if (_handKindString == "113")
			{
				this->kind = THREE_OF_A_KIND;
			}
			else if (_handKindString == "122")
			{
				this->kind = TWO_PAIR;
			}
		}
		else if (this->_cardCount.size() == 4)
		{
			this->kind = ONE_PAIR;
		}
	}

	void evaluate()
	{
		for (int i = 0; i < TOTAL_CARDS_ON_HAND; i++)
		{
			char card = this->_cards[i];
			int cardValue = CARD_MAP[card];
			int value = pow(NUMBER_BASE, TOTAL_CARDS_ON_HAND - (i + 1)) * cardValue;
			this->strength += value;

			if (!this->_cardCount.contains(card))
			{
				this->_cardCount.insert({card, 1});
				_handKindDistinctCard.push_back(card);
			}
			else
			{
				this->_cardCount[card]++;
			}
		}

		for (int i = 0; i < this->_cardCount.size(); i++)
		{
			_handKindCardCount.push_back(this->_cardCount[_handKindDistinctCard[i]]);
		}
		sort(_handKindCardCount.begin(), _handKindCardCount.end());

		for (int i = 0; i < _handKindCardCount.size(); i++)
		{
			_handKindString += to_string(_handKindCardCount[i]);
		}

		this->evaluateRule1();
	}

	void evaluate2()
	{
		int jokerCount = 0;
		for (int i = 0; i < TOTAL_CARDS_ON_HAND; i++)
		{
			char card = this->_cards[i];
			int cardValue = CARD_MAP2[card];
			int value = pow(NUMBER_BASE, TOTAL_CARDS_ON_HAND - (i + 1)) * cardValue;
			this->strength += value;

			if (!_cardCount.contains(card))
			{
				if (card == 'J')
				{
					jokerCount++;
				}
				else
				{
					_cardCount.insert({card, 1});
					_handKindDistinctCard.push_back(card);
				}
			}
			else
			{
				_cardCount[card]++;
			}
		}

		for (int i = 0; i < this->_cardCount.size(); i++)
		{
			_handKindCardCount.push_back(this->_cardCount[_handKindDistinctCard[i]]);
		}
		sort(_handKindCardCount.begin(), _handKindCardCount.end());

		for (int i = 0; i < _handKindCardCount.size(); i++)
		{
			_handKindString += to_string(_handKindCardCount[i]);
		}

		switch (jokerCount)
		{
		case 0:
			this->evaluateRule1();
			break;
		case 1:
			if (this->_cardCount.size() == 2)
			{
				if (_handKindString == "13")
				{
					this->kind = FOUR_OF_A_KIND;
				}
				else if (_handKindString == "22")
				{
					this->kind = FULL_HOUSE;
				}
			}
			else if (this->_cardCount.size() == 3)
			{
				if (_handKindString == "112")
				{
					this->kind = THREE_OF_A_KIND;
				}
			}
			else if (this->_cardCount.size() == 4)
			{
				this->kind = ONE_PAIR;
			}
			break;
		case 2:
			if (this->_cardCount.size() == 2)
			{
				if (_handKindString == "12")
				{
					this->kind = FOUR_OF_A_KIND;
				}
			}
			else if (this->_cardCount.size() == 3)
			{
				if (_handKindString == "111")
				{
					this->kind = THREE_OF_A_KIND;
				}
			}
			break;
		case 3:
			if (this->_cardCount.size() == 2)
			{
				if (_handKindString == "11")
				{
					this->kind = FOUR_OF_A_KIND;
				}
			}
			break;
		case 4:
		case 5:
			this->kind = FIVE_OF_A_KIND;
			break;
		default:
			break;
		}
		if (this->_cardCount.size() == 1)
		{
			this->kind = FIVE_OF_A_KIND;
		}
	}

public:
	HandKind kind;
	int strength;
	int bid;

	CardHand(string cards, int bid, bool part2 = false)
	{
		this->_cards = cards;
		this->bid = bid;
		this->strength = 0;
		this->kind = HIGH_CARD;

		if (!part2)
		{
			this->evaluate();
		}
		else
		{
			this->evaluate2();
		}
	}

	bool operator<(const CardHand &comparison) const
	{
		if (this->kind < comparison.kind)
			return true;
		if (this->kind > comparison.kind)
			return false;
		if (this->strength < comparison.strength)
			return true;

		return false;
	}
};

vector<string> tokenize(char *line)
{
	vector<string> result;
	char *token = strtok(line, " ");
	while (token != NULL)
	{
		result.push_back(token);
		token = strtok(NULL, " ");
	}

	return result;
}

vector<CardHand> setup(bool part2 = false)
{
	vector<CardHand> dataset;
	std::ifstream file("./input.txt");
	if (file.is_open())
	{
		while (file && !file.eof())
		{
			string line;
			getline(file, line);

			vector<string> tokens = tokenize(&line[0]);
			dataset.push_back(CardHand(tokens[0], stoi(tokens[1]), part2));
		}
	}
	return dataset;
}

void solve(vector<CardHand> dataset)
{
	int result = 0;
	sort(dataset.begin(), dataset.end());
	for (int i = 0; i < dataset.size(); i++)
	{
		result += (i + 1) * dataset[i].bid;
	}
	cout << result << endl;
}

int main()
{
	vector<CardHand> dataset = setup(true);
	solve(dataset);
	return 0;
}