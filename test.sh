#!/bin/bash

psql postgres -c "drop database tournament" ; psql postgres -c "create database tournament" && psql -f tournament.sql tournament && python tournament_test.py
