# RTR105
datormācības kursa elektroniskā klade
ctrl+alt+T -atver termināli
ctrl+shift+T -atverapakštermināli
ctrl+L -notīra termināli
uname -terminālī parāda operētājsistēmas nosaukumu
man komandas nos. -parāda komandas aprakstu
uname -a -pilns operētājsistēmas nosaukums
echo$ -atver bash termināli
whoami -parāda ,kas es esmu linux vidē
ctrl+alt+(f1-f7) -pieslēgšanās punkti sistēmā
pwd -parāda lokāciju failu sistēmā
l -al -visas direktorijas
history -parāda visu lietoto komandu vēsturi
history nosaukums .txt -nosūta komandu vēsturi uz noteiktu failu

17.09.18

es -a -parāda visus objektus mapē
cd -pārvietošanās failu direktorijā(p: cd Music -aiziet uz mapi Music)
ls -la detalizēta informācija par mapi
cd . -tekošā direktorija
cd .. -iziet no mapes
/ -root apgabala apzīmējums
Nokļūšana mājās
1) cd /home/user
2) cd ~(~ ir mājas apzīmējums)
3) cd 
Mapes veidošana
mkdir mapesnosaukums -izveido mapi
rmdir mapesnosaukums -dzēš mapi
rm -r mapesnosaukums -ļauj mapi nodēst ar visu saturu
echo -attēlo tekstu (echo "Teksts")
Teksta aizvietošana failā
echo "Teksts" >fails.txt -izveido failu, ja fails jau pastāv,tad tas tiek pārrakstīts
Faila satura apskatīšana
1)cat fails.txt
2)more fails.txt
3)less fails.txt

echo "Teksts" >>fails.txt -fails tiek papildināts
nano fails.txt -atver failu teksta redaktorā
Faila kopēšana
cp fails1.txt fails101.txt (fails1.txt-kopējamais fails; fails101.txt-pārkopētais fails)
Failu pārcelšana
mv *1*.txt Mape/ -pārcelt failus, kuru nos ir 1 uzn mapi
mv fails1.txt ..//fails101.txt -pārcelt un pārsaukt failu
mv fails101.txt fails102.txt -faila pārdēvēšana

es Mape/ -parāda mapes saturu
es -la Mape/ -parāda visus objektus mapē

26.9.18
nano mans_skripts.sh izveido skriptu, ļaij to reģidēt teksta redaktorā
cat mans_skripts.sh
chmod 767 mans_skripts.sh piešķir skriptam izpildvaru
Lai palaistu skriptu:
./mans_skripts.sh
/home/user/mans_skripts.sh
~/mans_skripts.sh
echo $PATH parāda caurskata mapes
PATH=$PATH:/home/user
git clone https://github.com/naurissilkans/RTR105 lejupielādēt manu githuba mapi
mv mans_skripts.sh RTR105/(VAR RAKSTĪT JAUNO FAILA NOSAUKUMU) pārvieto mans_skripts.sh uz RTR105 ar to pašu nosaukumu
cd RTR105
nano README.md atver failu readme.md teksta redaktorā
