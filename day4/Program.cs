using System;
using System.IO;
using System.Collections.Generic;

class ConsoleApp
{
  private class CardSet
  {
    private string[] _winningNumbers;
    private string[] _ownedNumbers;
    private int _matches;

    public int Matches
    {
      get { return _matches; }
    }

    public CardSet(string[] inWinning, string[] inOwned)
    {
      _winningNumbers = inWinning;
      _ownedNumbers = inOwned;
      _matches = 0;
      foreach (string owned in _ownedNumbers)
      {
        if (_winningNumbers.Any(item => owned == item))
        {
          _matches++;
        }
      }
    }
  }

  private static List<CardSet> Setup()
  {
    List<CardSet> cardSets = [];

    foreach (string line in File.ReadLines(@"./input.txt"))
    {
      string[] parts = line.Split(":");
      string[] numberSets = parts[1].Trim().Split("|");
      string[] winningNumbers = numberSets[0].Trim().Replace("  ", " ").Split(" ");
      string[] ownedNumbers = numberSets[1].Trim().Replace("  ", " ").Split(" ");
      cardSets.Add(new CardSet(winningNumbers, ownedNumbers));
    }

    return cardSets;
  }

  private static void Part1()
  {
    int points = 0;
    List<CardSet> cardSets = Setup();
    foreach (CardSet card in cardSets)
    {
      int matches = card.Matches;
      if (matches > 0)
      {
        int worth = (int)Math.Pow(2, (matches - 1));
        points += worth;
      }
    }

    Console.WriteLine("Part1: " + points);
  }

  private static void Part2()
  {
    List<CardSet> cardSets = Setup();
    Queue<int> indicesToProcess = new Queue<int>();

    for (int i = 0; i < cardSets.Count; i++)
    {
      indicesToProcess.Enqueue(i);
    }

    Func<int, List<int>> getCopyIndices = null;
    getCopyIndices = cardIndex =>
    {
      List<int> copyIndices = new List<int>();
      CardSet card = cardSets[cardIndex];
      int matches = card.Matches;
      if (matches > 0)
      {
        for (int i = 1; i <= matches; i++)
        {
          int copyIndex = cardIndex + i;
          copyIndices.Add(copyIndex);
        }
      }
      return copyIndices;
    };

    int score = 0;
    while (indicesToProcess.Count > 0)
    {
      int targetIndex = indicesToProcess.Dequeue();
      List<int> copyIndices = getCopyIndices(targetIndex);
      foreach (int copyIndex in copyIndices)
      {
        indicesToProcess.Enqueue(copyIndex);
      }
      score++;
    }

    Console.WriteLine("Part2: " + score);
  }

  static void Main(string[] args)
  {
    Part1();
    Part2();
  }
}