# Data from IPUSM
# Fields of importance: F, MIGPLACE5 (migration places from 5 years ago)

# LEGEND:

'''
britian 413, france 421, germany 453, mexico 200, japan 501, china 500
'''
'''
Code	Label	
1940
1pct
000	N/A	X
001	Alabama	X
002	Alaska	X
004	Arizona	X
005	Arkansas	X
006	California	X
008	Colorado	X
009	Connecticut	X
010	Delaware	X
011	District of Columbia	X
012	Florida	X
013	Georgia	X
015	Hawaii	X
016	Idaho	X
017	Illinois	X
018	Indiana	X
019	Iowa	X
020	Kansas	X
021	Kentucky	X
022	Louisiana	X
023	Maine	X
024	Maryland	X
025	Massachusetts	X
026	Michigan	X
027	Minnesota	X
Code	Label	
1940
1pct
028	Mississippi	X
029	Missouri	X
030	Montana	X
031	Nebraska	X
032	Nevada	X
033	New Hampshire	X
034	New Jersey	X
035	New Mexico	X
036	New York	X
037	North Carolina	X
038	North Dakota	X
039	Ohio	X
040	Oklahoma	X
041	Oregon	X
042	Pennsylvania	X
044	Rhode Island	X
045	South Carolina	X
046	South Dakota	X
047	Tennessee	X
048	Texas	X
049	Utah	X
050	Vermont	X
051	Virginia	X
053	Washington	X
054	West Virginia	X
Code	Label	
1940
1pct
055	Wisconsin	X
056	Wyoming	X
State group codes (1980 UR sample)	
061	Maine-New Hampshire-Vermont	·
062	Massachusetts-Rhode Island	·
063	Minnesota-Iowa-Missouri-Kansas-Nebraska-Dakotas	·
064	Maryland-Delaware	·
065	Montana-Idaho-Wyoming	·
066	Utah-Nevada	·
067	Arizona-New Mexico	·
068	Alaska-Hawaii	·
099	United States, not specified or state confidential	X
100	Americana Samoa	X
105	Guam	X
110	Puerto Rico	X
115	Virgin Islands	X
119	US outlying area	·
120	Other US possessions (1950)	·
150	Canada	·
151	English Canada	X
152	French Canada	X
155	St Pierre and Miquelon	·
160	Atlantic Islands	X
199	North America	·
200	Mexico	X
Code	Label	
1940
1pct
211	Belize/British Honduras	X
212	Costa Rica	X
213	El Salvador	·
214	Guatemala	X
215	Honduras	X
216	Nicaragua	X
217	Panama	X
218	Canal Zone	X
219	Central America, n.e.c.	X
250	Cuba	X
260	West Indies	·
261	Dominican Republic	X
262	Haiti	·
263	Jamaica	·
264	British West Indies	X
266	Trinidad and Tobago	·
267	Other West Indies	X
305	Argentina	X
310	Bolivia	X
315	Brazil	X
320	Chile	X
325	Colombia	X
330	Ecuador	·
345	Paraguay	·
350	Peru	X
Code	Label	
1940
1pct
360	Uruguay	·
365	Venezuela	X
370	North or Central America, n.s. (2000 5%)	·
390	South America, n.e.c.	X
400	Denmark	X
401	Finland	X
402	Iceland	·
404	Norway	X
405	Sweden	X
410	England	X
411	Scotland	X
412	Wales	X
413	United Kingdom	·
414	Ireland	X
415	Northern Ireland	X
420	Belgium	X
421	France	X
422	Liechtenstein	·
423	Luxembourg	X
424	Monaco	·
425	Netherlands	X
426	Switzerland	X
430	Albania	X
431	Andorra	·
432	Gibraltar	·
Code	Label	
1940
1pct
433	Greece	X
434	Dodecanese Islands	·
435	Italy	X
436	Portugal	X
437	Azores	X
438	Spain	X
439	Vatican City	·
440	Malta	·
450	Austria	X
451	Bulgaria	X
452	Czechoslovakia	X
453	Germany	X
454	Hungary	X
455	Poland	X
456	Romania	X
457	Yugoslavia	X
460	Estonia	X
461	Latvia	X
462	Lithuania	X
465	USSR	X
496	Byelorussia	·
498	Ukraine	·
499	Europe, n.s.	X
500	China	X
501	Japan	X
Code	Label	
1940
1pct
502	Korea	X
510	Brunei	·
511	Cambodia	·
512	Indonesia	·
513	Laos	·
514	Malaysia	·
515	Philippines	X
516	Singapore	·
517	Thailand	·
518	Vietnam	·
520	Afghanistan	·
521	India	X
525	Pakistan	·
522	Iran	·
523	Maldives	·
524	Nepal	·
530	Bahrain	·
531	Cyprus	·
532	Iraq	·
534	Israel/Palestine	X
535	Jordan	·
536	Kuwait	·
537	Lebanon	X
538	Oman	·
539	Qatar	·
Code	Label	
1940
1pct
540	Saudi Arabia	·
541	Syria	X
542	Turkey	X
543	United Arab Emirates	·
544	Yemen	·
548	Southwest Asia, n.e.c./n.s.	·
599	Asia, n.e.c./n.s.	X
600	Africa	X
610	Northern Africa	·
612	Egypt/United Arab Rep.	·
670	Central Africa	·
690	Southern Africa	·
694	South Africa (Union of)	·
699	Africa, n.e.c.	·
700	Coral Sea Islands	·
701	Australia	X
702	New Zealand	X
710	Pacific Islands	X
715	US Pacific Trust Territories	·
800	Heard and McDonald Islands	·
900	Abroad (unknown) or at sea	X
911	Abroad, n.s.	·
912	At sea	·
990	Same house	·
999	Missing/unknown

'''


import pandas as pd

# Read the data from the CSV file
data = pd.read_csv('data.csv')

# US Immigrants MIGPLAC5 between 00 and 120
usa_data = data[data['MIGPLAC5'] <= 120]
avg_USA_wage = usa_data.groupby('MIGPLAC5')['FWAGE1'].mean()

# Filter out MIGPLAC5 values between 00 and 120
filtered_data = data[data['MIGPLAC5'] > 120]

# Calculate the average wage for each MIGPLAC5
immigrants = filtered_data.groupby('MIGPLAC5')['FWAGE1'].mean()

# Print the results
print(avg_USA_wage)
print(immigrants)

# Output to file:
avg_USA_wage.to_csv('avg_USA_wage.csv')
immigrants.to_csv('immigrants.csv')

# Plot the results as a bar graph, USA, and Immigrants

# Get USA Average


# Get immigrants average

import matplotlib.pyplot as plt
plt.bar(avg_USA_wage.index, avg_USA_wage.values)
plt.bar(immigrants.index, immigrants.values)
plt.title('Average Wages (USA and Immigrants)')
plt.xlabel('MIGPLAC5')
plt.ylabel('Average Wage')
plt.legend()
plt.show()

