teams = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Flamengo', 'Vasco', 
'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 
'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 30)
print(f'Team list of Brasileiro {teams}')
print('-=' * 30)
print(f'The first teams are: {teams[:5]} ')
print('-=' * 30)
print(f'The last five are: {teams[-4:]}')
print('-=' * 30)
print(f'Teams in alfabetic order: {sorted(teams)}')
print('-=' * 30)
print(f'The chapecoense position is: {teams.index("Chapecoense")}')
