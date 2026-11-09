/* =====================================================================
   GUÍAS DE REEMPLAZO — datos
   Cada guía genera automáticamente (con semilla fija, siempre igual):
     1. Word search (sopa de letras) con todo el vocabulario
     2. Unscramble the words (palabras desordenadas + pista en español)
     3. Crossword (crucigrama) con las definiciones en inglés
     4. Sentence scramble (oraciones desordenadas)
     5. Odd one out (el intruso)
     6. Secret code (mensaje en clave numérica)
   vocab: [PALABRA, definición en inglés (crucigrama), pista en español]
   intrusos: grupos de 4; el intruso lleva *
   ===================================================================== */
const GUIAS_REEMPLAZO = [
/* ============================ 1° MEDIO · A1 ============================ */
{ id:"classroom", t:"Back to the Classroom", n:"1°", c:"A1", d:"Objetos de la sala, colores y lenguaje de clase.",
  vocab:[["PENCIL","You write and draw with it.","lápiz grafito"],["ERASER","It removes pencil mistakes.","goma"],["RULER","You draw straight lines with it.","regla"],["NOTEBOOK","You write your notes in it.","cuaderno"],["DESK","You sit at it in class.","pupitre"],["BOARD","The teacher writes on it.","pizarra"],["SCISSORS","You cut paper with them.","tijeras"],["GLUE","You stick paper with it.","pegamento"],["BACKPACK","You carry your books in it.","mochila"],["MARKER","A thick pen for the board.","plumón"],["CHAIR","You sit on it.","silla"],["BOOK","You read it.","libro"]],
  frases:["Open your books, please.","Can I borrow your ruler?","My backpack is blue and black.","How do you say goma in English?","The teacher writes on the board."],
  intrusos:[["pen","pencil","marker","*apple"],["red","blue","*chair","green"],["desk","*happy","chair","board"],["scissors","glue","*run","ruler"],["Monday","*notebook","Friday","Sunday"]],
  codigo:"ENGLISH IS FUN" },

{ id:"family-fun", t:"Family Puzzles", n:"1°", c:"A1", d:"Miembros de la familia y relaciones.",
  vocab:[["MOTHER","Your father's wife.","madre"],["FATHER","Your mother's husband.","padre"],["SISTER","Your parents' daughter (not you).","hermana"],["BROTHER","Your parents' son (not you).","hermano"],["UNCLE","Your father's brother.","tío"],["AUNT","Your mother's sister.","tía"],["COUSIN","Your uncle's child.","primo/a"],["GRANDMOTHER","Your mother's mother.","abuela"],["NEPHEW","Your sister's son.","sobrino"],["NIECE","Your brother's daughter.","sobrina"],["BABY","A very young child.","bebé"],["TWINS","Two brothers or sisters born on the same day.","gemelos"]],
  frases:["My mother is a nurse.","I have two cousins in Santiago.","My grandfather is seventy years old.","Do you have any brothers or sisters?","My aunt lives near the sea."],
  intrusos:[["mother","sister","aunt","*uncle"],["father","son","*niece","nephew"],["baby","*kitchen","cousin","twins"],["big","tall","*grandmother","short"],["he","she","they","*family"]],
  codigo:"I LOVE MY FAMILY" },

{ id:"animals", t:"Animal Kingdom", n:"1°", c:"A1", d:"Animales domésticos, salvajes y marinos.",
  vocab:[["DOG","A pet that barks.","perro"],["CAT","A pet that says meow.","gato"],["HORSE","You can ride this big animal.","caballo"],["ELEPHANT","A huge grey animal with a long nose.","elefante"],["MONKEY","It lives in trees and loves bananas.","mono"],["LION","The king of the jungle.","león"],["PENGUIN","A black and white bird that can't fly.","pingüino"],["WHALE","The biggest animal in the sea.","ballena"],["SNAKE","A long animal with no legs.","serpiente"],["RABBIT","It has long ears and eats carrots.","conejo"],["BIRD","It has wings and feathers.","pájaro"],["COW","It gives us milk.","vaca"]],
  frases:["My dog is very friendly.","Penguins live in Antarctica.","A whale is bigger than a shark.","Monkeys can climb trees.","Do you have a pet?"],
  intrusos:[["dog","cat","rabbit","*lion"],["whale","fish","dolphin","*horse"],["eagle","parrot","*snake","penguin"],["cow","*desk","sheep","pig"],["big","small","*monkey","fast"]],
  codigo:"ANIMALS ARE OUR FRIENDS" },

{ id:"food-fun", t:"Yummy Food!", n:"1°", c:"A1", d:"Comidas, frutas, verduras y bebidas.",
  vocab:[["APPLE","A red or green fruit.","manzana"],["BANANA","A long yellow fruit.","plátano"],["BREAD","You make sandwiches with it.","pan"],["CHEESE","A yellow food made from milk.","queso"],["CHICKEN","A bird we eat with rice or chips.","pollo"],["RICE","Small white grains; very popular in Asia.","arroz"],["SOUP","Hot liquid food you eat with a spoon.","sopa"],["WATER","The healthiest drink.","agua"],["TOMATO","A red vegetable in salads.","tomate"],["EGG","Chickens lay it.","huevo"],["MILK","A white drink from cows.","leche"],["FISH","It lives in the sea; we eat it on Fridays.","pescado"]],
  frases:["I have bread and cheese for breakfast.","My favourite fruit is banana.","Can I have a glass of water?","We eat fish on Fridays.","She doesn't like tomatoes."],
  intrusos:[["apple","banana","grape","*carrot"],["milk","juice","water","*bread"],["breakfast","lunch","dinner","*kitchen"],["salt","sugar","*spoon","pepper"],["hot","cold","*soup","sweet"]],
  codigo:"EAT FRUIT EVERY DAY" },

{ id:"body-fun", t:"Body Parts Challenge", n:"1°", c:"A1", d:"Partes del cuerpo y la cara.",
  vocab:[["HEAD","It is on top of your neck.","cabeza"],["EYES","You see with them.","ojos"],["EARS","You hear with them.","orejas"],["NOSE","You smell with it.","nariz"],["MOUTH","You eat and talk with it.","boca"],["TEETH","White things in your mouth.","dientes"],["HAND","It has five fingers.","mano"],["ARM","Between your shoulder and your hand.","brazo"],["LEG","You walk with it.","pierna"],["FOOT","You wear a shoe on it.","pie"],["KNEE","The middle part of your leg.","rodilla"],["SHOULDER","It is between your neck and arm.","hombro"]],
  frases:["I have two eyes and one nose.","Brush your teeth every day.","My knee hurts.","She has long black hair.","Wash your hands before lunch."],
  intrusos:[["eyes","nose","mouth","*knee"],["hand","finger","*foot","thumb"],["head","*shoe","arm","leg"],["teeth","*hat","lips","tongue"],["see","hear","smell","*hair"]],
  codigo:"HEAD SHOULDERS KNEES AND TOES" },

{ id:"jobs-fun", t:"Job Hunt", n:"1°", c:"A1", d:"Profesiones y oficios, incluidos los marítimos.",
  vocab:[["TEACHER","This person works in a school.","profesor"],["DOCTOR","This person helps sick people.","médico"],["NURSE","This person helps doctors in a hospital.","enfermera"],["COOK","This person prepares food.","cocinero"],["SAILOR","This person works on a ship.","marinero"],["CAPTAIN","The boss on a ship.","capitán"],["MECHANIC","This person repairs cars and engines.","mecánico"],["FARMER","This person works on a farm.","agricultor"],["PILOT","This person flies planes.","piloto"],["DIVER","This person works under the water.","buzo"],["FIREFIGHTER","This person puts out fires.","bombero"],["VET","An animal doctor.","veterinario"]],
  frases:["My father is a mechanic.","She works in a hospital.","I want to be a captain.","What does your mother do?","A pilot flies planes."],
  intrusos:[["doctor","nurse","*teacher","vet"],["sailor","captain","diver","*farmer"],["school","hospital","*pilot","farm"],["cook","*kitchen","waiter","chef"],["engine","*nurse","car","garage"]],
  codigo:"WORK HARD AND DREAM BIG" },

{ id:"time-days", t:"Time, Days & Months", n:"1°", c:"A1", d:"Días, meses, estaciones y la hora.",
  vocab:[["MONDAY","The first school day of the week.","lunes"],["FRIDAY","The day before Saturday.","viernes"],["SUNDAY","The day after Saturday.","domingo"],["JANUARY","The first month of the year.","enero"],["SEPTEMBER","The month of Fiestas Patrias in Chile.","septiembre"],["DECEMBER","The month of Christmas.","diciembre"],["SUMMER","The hottest season.","verano"],["WINTER","The coldest season.","invierno"],["CLOCK","It tells you the time.","reloj"],["HOUR","Sixty minutes.","hora"],["MORNING","The first part of the day.","mañana"],["NIGHT","When it's dark and we sleep.","noche"]],
  frases:["My birthday is in December.","We have English on Monday.","It's half past seven.","Summer is my favourite season.","I go to bed at ten o'clock."],
  intrusos:[["Monday","Tuesday","*March","Friday"],["spring","summer","*Sunday","winter"],["minute","hour","second","*month"],["January","*Thursday","May","June"],["morning","afternoon","*clock","night"]],
  codigo:"TIME IS GOLD" },

{ id:"countries-fun", t:"Around the World", n:"1°", c:"A1", d:"Países, nacionalidades e idiomas.",
  vocab:[["CHILE","A long country in South America.","Chile"],["PERU","Machu Picchu is in this country.","Perú"],["BRAZIL","People speak Portuguese here.","Brasil"],["MEXICO","Tacos come from this country.","México"],["JAPAN","Sushi comes from this country.","Japón"],["CHINA","The Great Wall is here.","China"],["FRANCE","The Eiffel Tower is here.","Francia"],["ITALY","Pizza and pasta come from here.","Italia"],["SPAIN","Its capital is Madrid.","España"],["ENGLAND","Big Ben is here.","Inglaterra"],["CANADA","A big cold country north of the USA.","Canadá"],["EGYPT","The pyramids are here.","Egipto"]],
  frases:["Where are you from?","I'm from Chile and I speak Spanish.","She is Brazilian.","They speak French in France.","My dream is to visit Japan."],
  intrusos:[["Chile","Peru","Brazil","*Spanish"],["English","French","*Italy","Chinese"],["Paris","London","Madrid","*Japan"],["Mexican","*Canada","Chilean","Peruvian"],["sea","ocean","*country","river"]],
  codigo:"HELLO FROM CHILE" },

{ id:"tobe-fun", t:"Verb To Be Games", n:"1°", c:"A1", d:"am / is / are con adjetivos de personalidad y descripción.",
  vocab:[["HAPPY","Feeling good; smiling.","feliz"],["TALL","Not short.","alto"],["FUNNY","This person makes you laugh.","divertido"],["KIND","Nice and friendly to others.","amable"],["TIRED","How you feel after a long day.","cansado"],["HUNGRY","When you want to eat.","con hambre"],["ANGRY","Feeling mad.","enojado"],["YOUNG","Not old.","joven"],["CLEVER","Intelligent.","inteligente"],["LAZY","This person doesn't like working.","flojo"],["SHY","This person doesn't talk much with new people.","tímido"],["BRAVE","Not afraid.","valiente"]],
  frases:["I am fifteen years old.","She is my best friend.","They are not at home.","Is he your brother?","We are very hungry."],
  intrusos:[["am","is","are","*have"],["happy","sad","angry","*table"],["he","she","it","*my"],["tall","short","*funny","big"],["isn't","aren't","*don't","I'm not"]],
  codigo:"YOU ARE AMAZING" },

/* ============================ 2° MEDIO · A2 ============================ */
{ id:"sports-fun", t:"Sports Mania", n:"2°", c:"A2", d:"Deportes, lugares y equipamiento deportivo.",
  vocab:[["FOOTBALL","Chile's most popular sport.","fútbol"],["TENNIS","You play it with a racket and a small ball.","tenis"],["SWIMMING","A sport in the pool.","natación"],["SURFING","You ride waves on a board.","surf"],["VOLLEYBALL","Two teams hit a ball over a net.","vóleibol"],["KARATE","A Japanese martial art.","karate"],["CYCLING","You do this sport on a bike.","ciclismo"],["REFEREE","The person who controls a match.","árbitro"],["COACH","The person who trains a team.","entrenador"],["TEAM","A group of players.","equipo"],["HELMET","You wear it on your head to protect it.","casco"],["MEDAL","Winners receive this.","medalla"]],
  frases:["We play football every Saturday.","She goes surfing in Reñaca.","The referee showed a red card.","Our team won the match.","Do you do any sport?"],
  intrusos:[["tennis","football","basketball","*swimming"],["racket","ball","net","*coach"],["pool","court","pitch","*helmet"],["karate","judo","*rugby","taekwondo"],["won","lost","scored","*play"]],
  codigo:"NEVER GIVE UP" },

{ id:"weather-fun", t:"Weather Watch", n:"2°", c:"A2", d:"El clima, las estaciones y el mar.",
  vocab:[["SUNNY","When the sun is shining.","soleado"],["RAINY","When water falls from the sky.","lluvioso"],["CLOUDY","The sky is grey and white.","nublado"],["WINDY","Good weather to fly a kite.","ventoso"],["FOGGY","You can't see well; it's like a white cloud.","neblinoso"],["STORM","Very bad weather with wind and rain.","tormenta"],["SNOW","White and cold; it falls in winter in the Andes.","nieve"],["UMBRELLA","You use it when it rains.","paraguas"],["SPRING","The season of flowers.","primavera"],["AUTUMN","The season when leaves fall.","otoño"],["THUNDER","The loud noise in a storm.","trueno"],["RAINBOW","Seven colours in the sky after rain.","arcoíris"]],
  frases:["What's the weather like today?","It's foggy in Valparaíso this morning.","Take an umbrella; it's going to rain.","Spring is my favourite season.","The storm closed the port."],
  intrusos:[["sunny","rainy","windy","*summer"],["spring","summer","autumn","*snow"],["hot","warm","*storm","cold"],["umbrella","coat","boots","*sun"],["thunder","lightning","rain","*rainbow"]],
  codigo:"AFTER THE RAIN COMES THE SUN" },

{ id:"feelings-fun", t:"How Do You Feel?", n:"2°", c:"A2", d:"Sentimientos y estados de ánimo.",
  vocab:[["EXCITED","Very happy because something good will happen.","entusiasmado"],["NERVOUS","How you feel before an exam.","nervioso"],["WORRIED","When you think about a problem a lot.","preocupado"],["PROUD","How you feel when you do something well.","orgulloso"],["BORED","When there's nothing to do.","aburrido"],["SCARED","How you feel in a horror film.","asustado"],["LONELY","Sad because you are alone.","solitario"],["RELAXED","Calm, without stress.","relajado"],["SURPRISED","When something unexpected happens.","sorprendido"],["UPSET","Sad and a bit angry.","molesto"],["CONFUSED","When you don't understand.","confundido"],["CALM","Quiet and peaceful.","tranquilo"]],
  frases:["I feel nervous before exams.","My parents are proud of me.","Why are you so upset?","She was surprised by the news.","Music helps me feel relaxed."],
  intrusos:[["happy","excited","proud","*bored"],["sad","lonely","upset","*calm"],["bored","tired","*happy","sleepy"],["scared","afraid","*brave","frightened"],["smile","laugh","*cry","joke"]],
  codigo:"BE KIND TO EVERYONE" },

{ id:"clothes-fun", t:"Fashion Puzzles", n:"2°", c:"A2", d:"Ropa, accesorios y compras.",
  vocab:[["JACKET","A short coat.","chaqueta"],["TROUSERS","You wear them on your legs.","pantalones"],["SKIRT","Girls and women wear it; it isn't trousers.","falda"],["DRESS","One piece of clothing for a party.","vestido"],["SWEATER","A warm piece of clothing made of wool.","chaleco"],["SCARF","You wear it around your neck in winter.","bufanda"],["GLOVES","You wear them on your hands.","guantes"],["BOOTS","Tall shoes for rain or snow.","botas"],["UNIFORM","Special clothes for school or work.","uniforme"],["SOCKS","You wear them inside your shoes.","calcetines"],["CAP","A hat for sun or sport.","jockey"],["SHIRT","It has buttons; you wear it with a tie.","camisa"]],
  frases:["Can I try this jacket on?","How much are these boots?","I'm wearing my school uniform.","It's too big for me.","She never wears a skirt."],
  intrusos:[["shirt","T-shirt","sweater","*shorts"],["scarf","gloves","coat","*sandals"],["boots","trainers","*cap","shoes"],["size","price","*wear","sale"],["cheap","expensive","*shop","new"]],
  codigo:"DRESS FOR SUCCESS" },

{ id:"house-fun", t:"Home Sweet Home", n:"2°", c:"A2", d:"Habitaciones de la casa y muebles.",
  vocab:[["KITCHEN","You cook here.","cocina"],["BEDROOM","You sleep here.","dormitorio"],["BATHROOM","You take a shower here.","baño"],["GARDEN","There are flowers and plants here.","jardín"],["SOFA","A comfortable seat for two or three people.","sofá"],["WARDROBE","You keep your clothes in it.","ropero"],["FRIDGE","It keeps food cold.","refrigerador"],["MIRROR","You see yourself in it.","espejo"],["SHOWER","You wash your body under it.","ducha"],["STAIRS","You go up and down on them.","escalera"],["LAMP","It gives light.","lámpara"],["PILLOW","You put your head on it in bed.","almohada"]],
  frases:["There is a sofa in the living room.","My bedroom is upstairs.","The fridge is in the kitchen.","Our house has a small garden.","Are there any chairs?"],
  intrusos:[["kitchen","bedroom","bathroom","*sofa"],["fridge","cooker","microwave","*bed"],["mirror","towel","shower","*pillow"],["roof","wall","window","*garden"],["upstairs","downstairs","*sleep","next to"]],
  codigo:"THERE IS NO PLACE LIKE HOME" },

{ id:"past-fun", t:"Past Tense Detectives", n:"2°", c:"A2", d:"Verbos irregulares en pasado simple.",
  vocab:[["WENT","Past of go.","fue"],["SAW","Past of see.","vio"],["ATE","Past of eat.","comió"],["BOUGHT","Past of buy.","compró"],["TOOK","Past of take.","tomó"],["MADE","Past of make.","hizo"],["CAME","Past of come.","vino"],["WROTE","Past of write.","escribió"],["DRANK","Past of drink.","bebió"],["FOUND","Past of find.","encontró"],["LEFT","Past of leave.","se fue"],["SLEPT","Past of sleep.","durmió"]],
  frases:["We went to Chiloé last summer.","I saw a whale yesterday.","She bought a new phone.","They didn't eat at home.","Where did you go last weekend?"],
  intrusos:[["went","saw","ate","*played"],["walked","visited","*took","cleaned"],["yesterday","last night","*tomorrow","ago"],["did","didn't","*does","was"],["bought","brought","thought","*bring"]],
  codigo:"YESTERDAY WAS A GREAT DAY" },

{ id:"travel-fun", t:"Let's Travel!", n:"2°", c:"A2", d:"Transporte, viajes y vacaciones.",
  vocab:[["PLANE","It flies in the sky.","avión"],["TRAIN","It travels on rails.","tren"],["FERRY","A boat that carries people and cars.","ferry / transbordador"],["TICKET","You buy it to travel.","pasaje"],["PASSPORT","You need it to visit other countries.","pasaporte"],["SUITCASE","You put your clothes in it for a trip.","maleta"],["AIRPORT","Planes arrive and leave here.","aeropuerto"],["HOTEL","You sleep here on holiday.","hotel"],["MAP","It shows you where places are.","mapa"],["BEACH","Sand and sea.","playa"],["TOURIST","A person on holiday in another place.","turista"],["CAMERA","You take photos with it.","cámara"]],
  frases:["We are going to travel by ferry.","Don't forget your passport!","The train leaves at nine.","I took many photos at the beach.","How much is a ticket to Santiago?"],
  intrusos:[["plane","train","bus","*ticket"],["airport","station","port","*suitcase"],["hotel","hostel","*beach","cabin"],["passport","*map","visa","ID card"],["drive","fly","sail","*sleep"]],
  codigo:"THE WORLD IS A BOOK" },

{ id:"routines-fun", t:"My Daily Routine", n:"2°", c:"A2", d:"Rutinas diarias, horas y adverbios de frecuencia.",
  vocab:[["WAKE","___ up: open your eyes in the morning.","despertar"],["SHOWER","You take one to get clean.","ducha"],["BREAKFAST","The first meal of the day.","desayuno"],["DRESSED","Get ___: put on your clothes.","vestido"],["BRUSH","___ your teeth.","cepillar"],["BUS","Many students go to school by ___.","bus"],["LUNCH","The meal at midday.","almuerzo"],["HOMEWORK","School work you do at home.","tarea"],["DINNER","The evening meal.","cena"],["ALWAYS","100% of the time.","siempre"],["NEVER","0% of the time.","nunca"],["SOMETIMES","Not always, not never.","a veces"]],
  frases:["I always get up at six o'clock.","She takes a shower after breakfast.","We never go to school on Sunday.","What time do you have lunch?","He usually does his homework at night."],
  intrusos:[["always","often","never","*today"],["breakfast","lunch","dinner","*bed"],["wake up","get up","*go to bed","get dressed"],["shower","toothbrush","soap","*bus"],["morning","afternoon","*weekend","evening"]],
  codigo:"EARLY TO BED EARLY TO RISE" },

{ id:"future-fun", t:"Future Fortune Tellers", n:"2°", c:"A2", d:"will / going to, planes y predicciones.",
  vocab:[["FUTURE","The time after now.","futuro"],["TOMORROW","The day after today.","mañana (día)"],["PLAN","Something you decide to do.","plan"],["ROBOT","A machine that can work like a person.","robot"],["PROMISE","You say you will do something for sure.","promesa"],["PREDICT","To say what will happen.","predecir"],["NEXT","___ week, ___ year.","próximo"],["SOON","In a short time.","pronto"],["DREAM","Something you want very much.","sueño"],["SPACE","Rockets travel here.","espacio"],["CAREER","Your job for many years.","carrera"],["MAYBE","Perhaps.","quizás"]],
  frases:["I'm going to study engineering.","I think robots will do many jobs.","I promise I will call you.","Look at the clouds; it's going to rain.","What are you going to do next summer?"],
  intrusos:[["will","won't","going to","*did"],["tomorrow","next week","soon","*yesterday"],["plan","dream","goal","*past"],["I'll","you'll","she'll","*I'm"],["robot","computer","*horse","rocket"]],
  codigo:"THE FUTURE IS YOURS" },

/* ===================== ESPECIAL MARÍTIMO · todos los niveles ===================== */
{ id:"ships-sea", t:"Ships & the Sea", n:"Todos", c:"A1–A2", d:"Vocabulario náutico: partes del barco y el mar.",
  vocab:[["SHIP","A big boat.","barco / buque"],["ANCHOR","It keeps the ship in one place.","ancla"],["DECK","The floor on top of a ship.","cubierta"],["CAPTAIN","The person in charge of the ship.","capitán"],["CREW","All the people who work on a ship.","tripulación"],["PORT","Ships arrive and leave here.","puerto"],["WAVE","Moving water in the sea.","ola"],["SAIL","Wind pushes it to move a boat.","vela"],["COMPASS","It shows north, south, east and west.","brújula"],["LIGHTHOUSE","A tower with a light to guide ships.","faro"],["MAST","The tall pole that holds the sails.","mástil"],["HARBOUR","A safe place for boats near the coast.","bahía / puerto"]],
  frases:["The ship is leaving the port.","The captain is on the deck.","The lighthouse guides the ships at night.","The crew is preparing the sails.","There are big waves today."],
  intrusos:[["ship","boat","ferry","*port"],["captain","sailor","cook","*anchor"],["north","south","east","*compass"],["wave","tide","current","*mast"],["deck","cabin","engine room","*beach"]],
  codigo:"FAIR WINDS AND FOLLOWING SEAS" },

{ id:"sea-animals", t:"Sea Creatures", n:"Todos", c:"A1–A2", d:"Animales marinos de las costas de Chile.",
  vocab:[["WHALE","The biggest animal in the world.","ballena"],["DOLPHIN","An intelligent sea mammal that jumps.","delfín"],["SHARK","A fish with many sharp teeth.","tiburón"],["OCTOPUS","It has eight arms.","pulpo"],["CRAB","It walks sideways.","cangrejo"],["SEAGULL","A white bird you see at the port.","gaviota"],["PENGUIN","A bird that swims but can't fly.","pingüino"],["SEAL","A sea animal with a fat body; it lives on rocks.","foca / lobo marino"],["TURTLE","A slow animal with a shell.","tortuga"],["JELLYFISH","A transparent sea animal that can sting.","medusa"],["STARFISH","A sea animal with five arms.","estrella de mar"],["PELICAN","A big bird with a big beak.","pelícano"]],
  frases:["Dolphins are very intelligent animals.","An octopus has eight arms.","There are many seagulls at the port.","Penguins can swim but they can't fly.","Whales are bigger than sharks."],
  intrusos:[["whale","dolphin","seal","*shark"],["seagull","pelican","penguin","*crab"],["octopus","*eagle","jellyfish","starfish"],["fins","shell","tentacles","*wings"],["swim","dive","float","*climb"]],
  codigo:"PROTECT THE OCEAN" },

{ id:"port-safety", t:"Safety on Board", n:"Todos", c:"A1–A2", d:"Seguridad a bordo e instrucciones (imperativos).",
  vocab:[["LIFEJACKET","You wear it to float in the water.","chaleco salvavidas"],["HELMET","It protects your head.","casco"],["GLOVES","They protect your hands.","guantes"],["ALARM","It makes a loud noise in an emergency.","alarma"],["EXIT","The door to go out.","salida"],["FIRE","It is hot and dangerous; it burns.","fuego"],["DANGER","A situation that can hurt you.","peligro"],["DRILL","Practice for an emergency.","simulacro"],["LIFEBOAT","A small boat to escape from a ship.","bote salvavidas"],["WARNING","A sign that tells you to be careful.","advertencia"],["SAFETY","Being protected from danger.","seguridad"],["RULES","Things you must or mustn't do.","reglas"]],
  frases:["Wear your lifejacket on the boat.","Don't run on the deck.","Listen to the captain's instructions.","Go to the nearest exit.","Never touch the engine without permission."],
  intrusos:[["helmet","gloves","boots","*fire"],["run","jump","*be careful","push"],["alarm","siren","whistle","*exit"],["wear","use","*don't","put on"],["danger","warning","*safety","risk"]],
  codigo:"SAFETY FIRST" },
];
