# chat

uruchomienie z terminala 
chmod +x ./run.sh
chmod +x ./upgradedb.sh
chmod +x ./initdb.sh

** jeżeli chce żeby nie był executable to -x


** instalowaliśmy packę eventlet (pip install..)

** Flask używa starej wersji http - 1.1, ale standardem wszędzie jest 2.0


** packa flaskowa defaultowo obsługuje coś co się nazywa namespace, ale ten defaultowy nie działa, dlatego trzeba przekazać
parametr namespace


./run.sh

Logic:

users
room 
field
okno z historia
autoryzacja i autentykacja
wykorzystanie protokołu websocket (nawiązuje połączenie z serverem) + nasłuchiwacz po stronie przeglądarki nasłuchuje
a nie http, które jest bezstanowe. 

pętle nieskończone w websocketach są robionę pętlami, ale te pętle nieskończone są w generatorze

mamy w websocketach async i await. Chodzi o to, że mamy asynchroniczne wykonywanie i nie blokuje się dopóki nie zostanie wykonany
await temu służy, żeby kod mógł wykonywać się dalej

async - to informacja, że to co jest przekazane jest robione asynchroniczne



