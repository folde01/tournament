#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    print '*** connect ***'
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    print '*** deleteMatches ***'
    db = connect()

    c = db.cursor()
    c.execute("select * from matches")
    print 'before: ', c.fetchall()

    c = db.cursor()
    c.execute("delete from matches")
    c.execute("select * from matches")
    print 'after: ', c.fetchall()

    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    print '*** deletePlayers ***'
    db = connect()
    c = db.cursor()
    c.execute("select * from players")
    print 'before: ', c.fetchall()
    c = db.cursor()
    c.execute("delete from players")
    db.commit()

    c.execute("select * from players")
    print 'after: ', c.fetchall()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    print '*** countPlayers ***'
    db = connect()
    c = db.cursor()
    #c.execute("select count(*) from players")
    c.execute("select * from players")
    #results = c.fetchone()[0]
    all = c.fetchall()
    print 'all: ', all
    c = db.cursor()
    c.execute("select count(*) from players")
    results = c.fetchall()[0][0]
    #results = c.fetchall()[0]
    #print c.fetchall()[0]
    #results = c.fetchall()
    print 'countPlayers:', results
    db.close()
    return results



def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    print '*** registerPlayer ***'
    db = connect()

    c = db.cursor()
    c.execute("select * from players")
    print 'before: ', c.fetchall()

    print 'inserting: ', name
    c.execute("insert into players (name) values (%s)", (name,))
    db.commit()

    c.execute("select * from players")
    print 'after: ', c.fetchall()

    #c.execute("select count(*) from players")
    #print c.fetchall()[0]
    #c.execute("select count(*) from players")
    #print c.fetchall()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    print '*** playerStandings ***'
    return [(0, 0, 0, 1), (0, 0, 0, 1)]



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    print '*** reportMatch ***'
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    print '*** swissPairings ***'


