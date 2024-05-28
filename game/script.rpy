define config.mouse = {}
define config.mouse['default'] = [('gui/cursors/pointer001.png', 0, 0)]

define wd = Character('Woody', color="#5c5030")
define bz = Character('Buzz', color="#742b99")
define js = Character('Jessie', color="#8c1f1f")
define pt = Character('Mr.Potato', color="#996b00")
define sd = Character('Sergente', color="#0f6100")

define audio.js1 = "audio/voices/Cantor/E Cantor/E 1 Cantor P.mp3"
define audio.js2 = "audio/voices/Cantor/E Cantor/E 2 Cantor P.mp3"
define audio.js3 = "audio/voices/Cantor/E Cantor/E 3 Cantor P.mp3"
define audio.js4 = "audio/voices/Cantor/E Cantor/E 4 Cantor P.mp3"
define audio.js5 = "audio/voices/Cantor/E Cantor/E 5 Cantor P.mp3"
define audio.js6 = "audio/voices/Cantor/E Cantor/E 6 Cantor P.mp3"
define audio.js31 = "audio/voices/Hotel/E Hotel/E 1 Hotel P.mp3"
define audio.js32 = "audio/voices/Hotel/E Hotel/E 2 Hotel P.mp3"
define audio.js33 = "audio/voices/Hotel/E Hotel/E 3 Hotel P.mp3"
define audio.js34 = "audio/voices/Hotel/E Hotel/E 4 Hotel P.mp3"
define audio.js35 = "audio/voices/Hotel/E Hotel/E 5 Hotel P.mp3"
define audio.js36 = "audio/voices/Hotel/E Hotel/E 6 Hotel P.mp3"
define audio.js37 = "audio/voices/Hotel/E Hotel/E 7 Hotel P.mp3"
define audio.sd1 = "audio/voices/Cantor/G Cantor/G 1 Cantor P.mp3"
define audio.sd2 = "audio/voices/Cantor/G Cantor/G 2 Cantor P.mp3"
define audio.sd3 = "audio/voices/Cantor/G Cantor/G 3 Cantor P.mp3"
define audio.sd4 = "audio/voices/Cantor/G Cantor/G 4 Cantor P.mp3"
define audio.sd5 = "audio/voices/Cantor/G Cantor/G 5 Cantor P.mp3"
define audio.sd6 = "audio/voices/Cantor/G Cantor/G 6 Cantor P.mp3"
define audio.wd21 = "audio/voices/Euclide/G Euclide/G 1 Euclide P.mp3"
define audio.wd22 = "audio/voices/Euclide/G Euclide/G 2 Euclide P.mp3"
define audio.wd23 = "audio/voices/Euclide/G Euclide/G 3 Euclide P.mp3"
define audio.wd24 = "audio/voices/Euclide/G Euclide/G 4 Euclide P.mp3"
define audio.wd31 = "audio/voices/Hotel/G Hotel/G 1 Hotel P.mp3"
define audio.wd32 = "audio/voices/Hotel/G Hotel/G 2 Hotel P.mp3"
define audio.wd33 = "audio/voices/Hotel/G Hotel/G 3 Hotel P.mp3"
define audio.wd34 = "audio/voices/Hotel/G Hotel/G 4 Hotel P.mp3"
define audio.wd35 = "audio/voices/Hotel/G Hotel/G 5 Hotel P.mp3"
define audio.wd36 = "audio/voices/Hotel/G Hotel/G 6 Hotel P.mp3"
define audio.wd37 = "audio/voices/Hotel/G Hotel/G 7 Hotel P.mp3"
define audio.wd38 = "audio/voices/Hotel/G Hotel/G 8 Hotel P.mp3"
define audio.wd39 = "audio/voices/Hotel/G Hotel/G 9 Hotel P.mp3"
define audio.bz1 = "audio/voices/Cantor/R Cantor/R 1 Cantor P.mp3"
define audio.bz2 = "audio/voices/Cantor/R Cantor/R 2 Cantor P.mp3"
define audio.bz3 = "audio/voices/Cantor/R Cantor/R 3 Cantor P.mp3"
define audio.bz4 = "audio/voices/Cantor/R Cantor/R 4 Cantor P.mp3"
define audio.bz5 = "audio/voices/Cantor/R Cantor/R 5 Cantor P.mp3"
define audio.bz6 = "audio/voices/Cantor/R Cantor/R 6 Cantor P.mp3"
define audio.bz7 = "audio/voices/Cantor/R Cantor/R 7 Cantor P.mp3"
define audio.bz8 = "audio/voices/Cantor/R Cantor/R 8 Cantor P.mp3"
define audio.bz31 = "audio/voices/Hotel/R Hotel/R 1 Hotel P.mp3"
define audio.bz32 = "audio/voices/Hotel/R Hotel/R 2 Hotel P.mp3"
define audio.bz33 = "audio/voices/Hotel/R Hotel/R 3 Hotel P.mp3"
define audio.bz34 = "audio/voices/Hotel/R Hotel/R 4 Hotel P.mp3"
define audio.bz35 = "audio/voices/Hotel/R Hotel/R 5 Hotel P.mp3"
define audio.bz36 = "audio/voices/Hotel/R Hotel/R 6 Hotel P.mp3"
define audio.bz37 = "audio/voices/Hotel/R Hotel/R 7 Hotel P.mp3"
define audio.bz38 = "audio/voices/Hotel/R Hotel/R 8 Hotel P.mp3"
define audio.bz39 = "audio/voices/Hotel/R Hotel/R 9 Hotel P.mp3"
define audio.bz321 = "audio/voices/Hotel/R Hotel/R 10 Hotel P.mp3"
define audio.pt21 = "audio/voices/Euclide/M Euclide/M 1 Euclide P.mp3"
define audio.pt22 = "audio/voices/Euclide/M Euclide/M 2 Euclide P.mp3"
define audio.pt23 = "audio/voices/Euclide/M Euclide/M 3 Euclide P.mp3"
define audio.pt24 = "audio/voices/Euclide/M Euclide/M 4 Euclide P.mp3"
define audio.pt25 = "audio/voices/Euclide/M Euclide/M 5 Euclide P.mp3"
define audio.wdbz1 = "audio/voices/Hotel/GR Hotel/G R 1 Hotel P.mp3"

define audio.intro = "audio/music/Intro.mp3"

init:
    $ left1 = Position(xalign=0.3, yalign=1.5)
    $ left2 = Position(xalign=0.2, yalign=1.5)
    $ right1 = Position(xalign=0.7, yalign=1.5)
    $ right2 = Position(xalign=0.9, yalign=1.5)
    $ center1 = Position(xalign=0.5, yalign=1.5)
    transform text1:
        yalign 1.5
        linear 15.0 yalign -1.5


label start:
    scene bg soldiers with fade
    show js normal at left with dissolve
    play music intro fadein 2
    play audio js1 volume 0.2
    js "Oh no! le truppe del sergente si sono mescolate con le truppe nemiche."
    show sd normal at right with moveinright
    stop music fadeout 5
    play audio sd1
    sd "È terribile! Truppa abortire, abortire, tornare alla base ora immediatamente!!"
    play audio js2
    js "Come faremo ora a distinguere un soldato da un altro?"
    play audio sd2
    sd "Ci vorrebbe un’idea!"
    play audio js3
    js "Buzz tu che ne pensi?"
    show bz normal at left1 with moveinleft
    play audio bz1 volume 1.3
    bz "Potremmo associare a ogni soldato un soldato dell'altro esercito in modo tale da dispiegarli tutti e poterli così dividere."
    play audio sd3
    sd "Mi sembra un’ottima idea! Soldati disporsi uno a fianco all’altro."
    play audio js4
    js "Buzz toglimi una curiosità ma se avessimo avuto infiniti soldati sarebbe stata la stessa cosa?"
    play audio bz2
    bz "Beh dipende, se i due insiemi hanno le stesse dimensioni, cioè se ogni elemento di un insieme può essere associato ad un elemento dell’altro, allora la risposta è sì."
    play audio js5
    js "E se non fosse così?"
    play audio bz3
    bz "In questo caso stiamo parlando di due insieme infiniti ma di diverse dimensioni."
    play audio sd4
    sd "Non sto capendo, potresti farmi un esempio?"
    play audio bz4
    bz "Certo."
    scene bg expo2 with fade
    show bz normal at left with moveinleft
    play audio bz5
    bz "Prendiamo come esempio l’insieme dei numeri naturali, quelli contabili, e l’insieme dei numeri reali."
    play audio bz6
    bz "Ipotizziamo per assurdo di poter associare ogni numero reale ad ogni numero naturale, possiamo ottenere questa relazione: 1 si associa al numero reale R1, 2 a R2 eccetera, quindi N1 R1, N2 R2, N3 R3, e così via."
    play audio sd5
    sd "Non capisco dove stia la differenza, non si associano anche qui i vari elementi dei diversi insiemi?"
    play audio bz7
    bz "Purtroppo no l’insieme dei numeri reali viene definito denso. Per esempio, fra 2 e 3 possiamo avere infiniti numeri intermedi, come 2,4-2,63 e infiniti altri, perciò, non sarà possibile associare ogni numero reale con ogni numero naturale."
    scene bg soldiers with fade
    show js normal at left
    show sd normal at right
    show bz normal at left1
    with dissolve
    play audio sd6
    sd "Grazie Buzz, da oggi in poi avrò una visione diversa dell’infinito."
    play audio js6
    js "Sei il migliore Buzz."
    play audio bz8
    bz "Grazie ragazzi, è un piacere parlare con voi."
    hide bz normal
    hide js normal
    with moveoutleft
    hide sd normal with moveoutright

    scene bg room1 with fade
    show wd happy at right1 with moveinright
    play music intro fadein 2
    play audio wd21
    wd "Gentili telespettatori, Donne, Uomini, Bambini, Bambine, Cani, Gatti e chi più ne ha più ne metta, ecco a voi il professor Mr. Potato con la sua spiegazione della dimostrazione di Euclide."
    scene bg expo1 with fade
    show pt normal at left with moveinleft
    stop music fadeout 5
    play audio pt21 volume 1.7
    pt "Grazie mille dell’ospitalità. Ipotizziamo per assurdo i numeri primi come un insieme di numeri finito che vada da P1 a Pn. Ora calcoliamo il prodotto P di questi numeri a cui sommiamo uno, definendo questo valore Q. tutto chiaro?"
    play audio wd22
    wd "Finora la seguiamo professore."
    play audio pt22 volume 1.7
    pt "Ora ci troviamo difronte ad un bivio: Se Q fosse un numero primo, dimostriamo che esistono altri numeri primi; se Q non fosse un numero primo, comunque non sarà divisibile per i numeri primi dell’insieme, in quanto Q è definito come il prodotto di questi numeri aumentato di uno."
    play audio pt23 volume 1.7
    pt "Nel caso Q non fosse un numero primo, dovrà quindi esistere un altro suo divisore primo non compreso nell’insieme: dimostrando così l’esistenza di un altro numero primo."
    play audio wd23 
    wd "Lei quindi mi sta dicendo che esistono infiniti numeri primi?"
    play audio pt24 volume 1.7
    pt "Certo, questa dimostrazione è ripetibile infinite volte dimostrando così l’infinità dei numeri primi."
    scene bg room1 with fade
    show wd normal at right1 with dissolve
    play audio wd24
    wd "La ringrazio del tempo a noi dedicato, è stato davvero un piacere averla qui."
    show pt normal at left1 with moveinleft
    play audio pt25 volume 1.7
    pt "Il piacere è mio grazie infinite e buona continuazione."
    hide pt normal with moveoutleft
    hide wd normal with moveoutright

    scene bg room2 with fade
    show bz normal at left2 with moveinleft
    show wd normal at right1 with moveinright
    play music intro fadein 2
    play audio bz31
    bz "Ciao Woody… come va?"
    play audio wd31
    wd "Ei Buzz… tutto bene grazie, tu come stai?"
    stop music fadeout 5
    play audio bz32
    bz "Non c’è male, come mai da queste parti?"
    play audio wd32
    wd "Ho da poco cambiato casa e ne ho presa una bellissima! La sto ancora ristrutturando però. E devo assolutamente prendere una stanza in Hotel. Tu ne conosci uno bello ed economico?"
    play audio bz33
    bz "Certo ti consiglio il grande Hotel Di Hilbert, di sicuro c’è una stanza per te."
    play audio wd33
    wd "Sembra davvero un bel posto mi accompagneresti?"
    play audio bz34
    bz "Certo salta su…"
    hide wd normal with moveoutright
    hide bz normal with moveoutleft

    scene bg reception with fade
    show wd normal at left
    show bz normal at left1
    with moveinleft
    play audio wdbz1 volume 2.0
    "Buzz / Woody" "Permesso, Buongiorno!"
    show js normal at right2 with moveinright
    play audio js31
    js "Buongiorno signori e ben venuti al grande Hotel Di Hilbert, qui il posto è assicurato, come posso aiutarvi?"
    play audio wd34
    wd "Salve vorrei una camera singola per questa notte, sarebbe disponibile?"
    play audio js32
    js "Controllo subito e le dico. Allora purtroppo noi abbiamo infiniti ospiti questa giornata e le nostre infinite camere sono tutte occupate."
    play audio bz35
    bz "Mi scusi lei ha detto che ha infinite camere?"
    play audio js33
    js "Certo noi abbiamo moltissime camere."
    play audio bz36
    bz "Non dovrebbe essere un problema: dato che solo una persona in più ha bisogno di una camera, basterà che gli altri ospiti si spostino ognuno in una camera più avanti… Fino a qui tutto chiaro?"
    play audio js34
    js "Per ora sì signore…"
    play audio bz37
    bz "Bene di conseguenza ogni cliente si sposterà dalla camera N alla camera N+1 e così via per un qualunque numero finito di clienti da ospitare."
    play audio wd35
    wd "Interessante, mi togli una curiosità Buzz… e se dovessero arrivare un numero infinito di persone?"
    scene cg hotel1 with fade
    play audio bz38
    bz "Beh semplice, in quel caso ogni ospite già presente si dovrà spostare dalla camera in cui si trova nella camera con il numero doppio. Da N a 2N, quindi tutti gli ospiti già presenti occuperanno le stanze di numeri pari e i nuovi infiniti ospiti potranno sistemarsi nelle camere di numeri dispari."
    scene bg reception with fade
    show wd normal at left
    show bz normal at left1
    show js normal at right2
    with dissolve
    play audio js35
    js "Beh, il personale dovrebbe essere preparato nell’ipotetico caso dovessero presentarsi un infinito numero di autobus con infiniti numeri di passeggeri."
    play audio wd36
    wd "Davvero!"
    scene cg hotel2 with fade
    play audio bz39
    bz "Eh già, basterà che gli ospiti già presenti si spostino nella stanza 2 elevato alla N. Gli ospiti del primo bus nella stanza 3 elevato alla N e così via, dato che la potenza di un numero primo non è potenza di nessuno altro numero primo e data l’infinità di questi ultimi, si avranno stanze sempre diverse."
    scene bg reception with fade
    show wd normal at left
    show bz normal at left1
    show js normal at right2
    with dissolve
    play audio js36
    js "Mi scusi signore, ecco a lei chiavi e telecomando della sua camera…"
    play audio wd37
    wd "Grazie, è stata davvero molto gentile."
    play audio js37
    js "La ringrazio e buona permanenza nel nostro Hotel."
    hide js normal with moveoutright
    play audio wd38
    wd "Grazie Buzz…"
    play audio bz321
    bz "Ciao Woody... buona notte."
    play audio wd39
    wd "Notte!!"
    hide wd normal
    hide bz normal
    with moveoutleft
    jump credits
    return

label credits:
    scene black with dissolve
    show text "Grazie tante per la lettura {p} Spero che vi si è piacuto {p} il nostro lavoro {p}{p} Il nostro gruppo:{p} Giovanni de Angelis {p} Riccardo Blanco {p} Mykhailo Onufriiev {p} Elisa Valenti" at text1
    pause 10
    return