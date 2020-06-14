#encoding "utf8"


//Достопримечательности

//Авангард
Avangard -> 'авангард';
Attractions -> Avangard<h-reg1>;

//Площадь Павших Борцов
Place -> 'площадь';
Attractions -> Place<gnc-agr[1], rt> Adj<h-reg1, gnc-agr[1]> Noun<h-reg1, gnc-agr[1]> ;

//Библиотека Горького(доделать)
Bibl_Gor_1 -> 'библиотека';
Bibl_Gor_2 -> 'горький';
Attractions -> Bibl_Gor_1 AnyWord* Bibl_Gor_2<h-reg1>;

//Памятник Саше Филиппову
Monument_SF_1 -> 'памятник';
Monument_SF_2 -> 'саша';
Attractions -> Monument_SF_1 Monument_SF_2<h-reg1> AnyWord<wff=/(Филиппову)/>; 

//Музей истории Кировского района
Museum_His_Kir_1 -> 'музей';
Museum_His_Kir_2 -> 'история';
Museum_His_Kir_3 -> 'кировский';
Museum_His_Kir_4 -> 'район';
Attractions -> Museum_His_Kir_1 Museum_His_Kir_2 Museum_His_Kir_3<h-reg1> Museum_His_Kir_4;

//Памятник Чекистам
Monument_CH_1 -> 'памятник';
Monument_CH_2 -> 'чекист';
Attractions -> Monument_CH_1 Monument_CH_2;
//Армянская церковь Святого Георгия
Arm_church_1 -> 'армянский';
Arm_church_2 -> 'церковь';
Arm_church_3 -> 'святой';
Arm_church_4 -> 'георгий';
Attractions -> Arm_church_1 Arm_church_2 Arm_church_3<h-reg1> Arm_church_4<h-reg1>;
//Трамвай-памятник
Tram_Monument -> 'трамвай-памятник';
Attractions -> Tram_Monument;
//Воинский эшелон
Military_Train_1 -> 'воинский';
Military_Train_2 -> 'эшелон';
Attractions -> Military_Train_1<gnc-agr[1]> Military_Train_2<gnc-agr[1], rt>;
//Мельница Гергардта
Mill_1 -> 'мельница';
Attractions -> Mill_1 Word<wff=/Гергардта/>; 
//Памятник Дзержинскому
Monument_DZ_1 -> 'памятник';
Monument_DZ_2 -> 'дзержинский';
Attractions -> Monument_DZ_1 Monument_DZ_2<h-reg1>;
//Здание Царицынской пожарной команды
Building_Tsar_pozh_1 -> 'здание';
Building_Tsar_pozh_2 -> 'царицынский';
Building_Tsar_pozh_3 -> 'пожарный';
Building_Tsar_pozh_4 -> 'команда';
Attractions -> Building_Tsar_pozh_1 Building_Tsar_pozh_2<h-reg1> Building_Tsar_pozh_3 Building_Tsar_pozh_4;
//Дом Павлова
House_Pavlova -> 'дом';
Attractions -> House_Pavlova AnyWord<wff=/Павлова/>;
//Челябинский колхозник
Chel_Col_1 -> 'челябинский';
Chel_Col_2 -> 'колхозник';
Attractions -> Chel_Col_1<gnc-agr[1]> Chel_Col_2<gnc-agr[1]>;
//Памятник Гоголю
Monument_Gogol_1 -> 'памятник';
Monument_Gogol_2 -> Word<wff=/Гоголю/>;
Attractions -> Monument_Gogol_1 Monument_Gogol_2;
//БК-13
BK_13 -> AnyWord<wff=/(БК-13)/>;
Attractions -> BK_13;
//Бейт Давид
BD_1 -> 'бейт';
BD_2 -> 'давид';
Attractions -> BD_1<h-reg1> BD_2<h-reg1>;
//Бармалей
Barm -> 'бармалей';
Attractions_Full -> Barm interp (Fact.Attractions::not_norm);
//Лысая гора
B_Mountain_1 -> 'лысый';
B_Mountain_2 -> 'гора';
Attractions -> B_Mountain_1<h-reg1, gnc-agr[1]> B_Mountain_2<gnc-agr[1]>;
//Элеватор
Elevator -> 'элеватор';
Attractions -> Elevator;
//Памятник Паникахе
Monument_Panikaha_1 -> 'памятник';
Monument_Panikaha_2 -> Word<wff=/(Паникахе)/>;
Attractions -> Monument_Panikaha_1 (AnyWord<gram="persn">) Monument_Panikaha_2;
//Казанский кафедральный собор
Kazan_Cathedral_1 -> 'казанский';
Kazan_Cathedral_2 -> 'собор';
Attractions -> Kazan_Cathedral_1<h-reg1, gnc-agr[1]> (Adj<gnc-agr[1]>*) Kazan_Cathedral_2<gnc-agr[1], rt>;
//Фонтан влюбленных
Fountain_Love_1 -> 'фонтан';
Fountain_Love_2 -> Word<wff=/(влюбленных)/>;
Attractions -> Fountain_Love_1 Fountain_Love_2;
//Музей-квартира Луконина М.К.
Museum_House_1 -> 'музей-квартира';
Museum_House_2 -> Word<wff=/(Луконина)/>;
Attractions -> Museum_House_1 Museum_House_2;
//Музейно-выставочный центр Красноармейского района
Museum_RedArm_1 -> 'музейно-выставочный';
Museum_RedArm_2 -> 'центр';
Museum_RedArm_3 -> 'красноармейский';
Museum_RedArm_4 -> 'район';
Attractions -> Museum_RedArm_1 Museum_RedArm_2 Museum_RedArm_3 Museum_RedArm_4;
//Мамаев курган
Mamaev_Kurgan_1 -> Word<wff=/(Мамаев)/>;
Mamaev_Kurgan_2 -> 'курган';
Attractions -> Mamaev_Kurgan_1 Mamaev_Kurgan_2;
//Речной порт
River_Port_1 -> 'речной';
River_Port_2 -> 'порт';
Attractions -> River_Port_1<gnc-agr[1]> River_Port_2<gnc-agr[1], rt>;
//Царицынская опера
Tsaritsyn_Opera_1 -> 'царицынский';
Tsaritsyn_Opera_2 -> 'опера';
Attractions -> Tsaritsyn_Opera_1<gnc-agr[1]> Tsaritsyn_Opera_2<gnc-agr[1], rt>;
//Музей истории здравоохранения
Museum_HH_1 -> 'музей';
Museum_HH_2 -> 'история';
Museum_HH_3 -> 'здравоохранение';
Attractions -> Museum_HH_1 Museum_HH_2 Museum_HH_3;
//Музей "Дети Царицына, Сталинграда, Волгограда"
Museum_Child_1 -> 'музей';
Museum_Child_2 -> AnyWord<wff=/Дети/>;
Museum_Child_3 -> AnyWord<wff=/Волгограда/>;
Attractions -> Museum_Child_1 Museum_Child_2 AnyWord+ Museum_Child_3;

//Народный музей Волгоградских железнодорожников
People_Museum_1 -> 'народный';
People_Museum_2 -> 'музей';
People_Museum_3 -> 'волгоградский';
People_Museum_4 -> Word<wff=/железнодорожников/>;
Attractions -> People_Museum_1<gnc-agr[1]> People_Museum_2<gnc-agr[1], rt> People_Museum_3 People_Museum_4;
//Музей авиации
Aviation_Museum_1 -> 'музей';
Aviation_Museum_2 -> Word<wff=/авиации/>;
Attractions -> Aviation_Museum_1 (Word) Aviation_Museum_2;
//Выставочный зал Волгоградского музея изобразительных искусств им. И.И.Машкова
Mashkov_EH_1 -> 'выставочный';
Mashkov_EH_2 -> 'зал';
Mashkov_EH_3 -> Word<wff=/Машкова/>;
Attractions -> Mashkov_EH_1<gnc-agr[1]> Mashkov_EH_2<gnc-agr[1], rt> AnyWord* Mashkov_EH_3;
//Военно-патриотический музей истории связи и радиолюбительства Царицына-Сталинграда-Волгограда
MP_Museum_1 -> 'военно-патриотический';
MP_Museum_2 -> AnyWord<wff=/Царицына-Сталинграда-Волгограда/>;
Attractions -> MP_Museum_1 AnyWord* MP_Museum_2;
//Музей "истории Волго-Донского судоходного канала"
VD_Museum_1 -> 'музей';
VD_Museum_2 -> 'история';
VD_Museum_3 -> AnyWord<wff=/Волго-Донского/>;
VD_Museum_4 -> 'судоходный';
VD_Museum_5 -> 'канал';
Attractions -> VD_Museum_1 VD_Museum_2 VD_Museum_3 VD_Museum_4 VD_Museum_5;
//Парк имени Юрия Гагарина
Park_Yuri_Gagarin_1 -> 'парк';
Park_Yuri_Gagarin_2 -> 'имя';
Park_Yuri_Gagarin_3 -> 'юрий';
Park_Yuri_Gagarin_4 -> 'гагарин';
Attractions -> Park_Yuri_Gagarin_1 (Word) Park_Yuri_Gagarin_2 (Park_Yuri_Gagarin_3<h-reg1>) Park_Yuri_Gagarin_4<h-reg1>;
//Выставочный зал Волгоградской областной организации союза художников России
EH_Artists_1 -> 'выставочный';
EH_Artists_2 -> 'зал';
EH_Artists_3 -> 'художник';
EH_Artists_4 -> AnyWord<wff=/России/>;
Attractions -> EH_Artists_1<gnc-agr[1]> EH_Artists_2<gnc-agr[1], rt> AnyWord* EH_Artists_3 EH_Artists_4;

//Парк Победы
Victory_Park_1 -> 'парк';
Victory_Park_2 -> 'победа';
Attractions -> Victory_Park_1 Victory_Park_2<h-reg1>;
//Комсомольский сад
Coms_Garden_1 -> 'комсомольский';
Coms_Garden_2 -> 'сад';
Attractions -> Coms_Garden_1<gnc-agr[1], h-reg1> Coms_Garden_2<gnc-agr[1], rt>;
//Детский городской парк
Child_Park_1 -> 'детский';
Child_Park_2 -> 'городской';
Child_Park_3 -> 'парк';
Attractions -> Child_Park_1<gnc-agr[1]> Child_Park_2<gnc-agr[1]> Child_Park_3<gnc-agr[1], rt>;
//Сквер имени Саши Филиппова
Square_1 -> 'сквер';
Square_2 -> 'имя';
Square_3 -> 'саша';
Square_4 -> AnyWord<wff=/Филиппова/>;
Attractions -> Square_1 Square_2 Square_3 Square_4;
//Парк Дружбы: "Волгоград-Баку"
Park_Fr_1 -> 'парк';
Park_Fr_2 -> 'дружба';
Park_Fr_3 -> Word<wff=/Волгоград-Баку/>;
Attractions -> Park_Fr_1 Park_Fr_2 AnyWord* Park_Fr_3 ;
//Зал Воинской Славы
Military_HF_1 -> 'зал';
Military_HF_2 -> 'воинский';
Military_HF_3 -> 'слава';
Attractions ->  Military_HF_1 Military_HF_2 Military_HF_3;
//Ботанический сад ВГСПУ
Botanic_Garden_1 -> 'ботанический';
Botanic_Garden_2 -> 'сад';
Botanic_Garden_3 -> Word<wff=/ВГСПУ/>;
Attractions -> Botanic_Garden_1<gnc-agr[1]> Botanic_Garden_2<gnc-agr[1], rt> Botanic_Garden_3;
//ЦПКиО
Attractions -> Word<wff=/ЦПКиО/>;
//Музей музыкальных инструментов им. Е.Н. Пушкина
Museum_Pushkin_1 -> 'музей';
Museum_Pushkin_2 -> 'музыкальный';
Museum_Pushkin_3 -> 'инструмент';
Museum_Pushkin_4 -> Word<wff=/Пушкина/>;
Attractions -> Museum_Pushkin_1 Museum_Pushkin_2 Museum_Pushkin_3 AnyWord* Museum_Pushkin_4;
//Музей мер и весов
Museum_MV_1 -> 'музей';
Museum_MV_2 -> 'мера';
Museum_MV_3 -> 'весы';
Attractions -> Museum_MV_1 Museum_MV_2 SimConjAnd Museum_MV_3;
//Областной краеведческий музей
Regional_Museum_1 -> 'областной';
Regional_Museum_2 -> 'краеведческий';
Regional_Museum_3 -> 'музей';
Attractions -> Regional_Museum_1<gnc-agr[1]> Regional_Museum_2<gnc-agr[1]> Regional_Museum_3<gnc-agr[1], rt>;
//Музей-заповедник "Старая Сарепта"
Museum_OS_1 -> 'музей-заповедник';
Museum_OS_2 -> AnyWord<wff=/Сарепта/>;
Attractions -> Museum_OS_1 AnyWord* Museum_OS_2;
//Планетарий
Planetarium -> 'планетарий';
Attractions -> Planetarium;
//Волгоградский музей изобразительных искусств им. И.И. Машкова
Mashkov_Arts_1 -> 'волгоградский';
Mashkov_Arts_2 -> 'музей';
Mashkov_Arts_3 -> Word<wff=/Машкова/>;
Attractions -> Mashkov_Arts_1<gnc-agr[1]> Mashkov_Arts_2<gnc-agr[1], rt> AnyWord* Mashkov_Arts_3;
//Волгоградская областная филармония
Philharmonic_1 -> 'волгоградский';
Philharmonic_2 -> 'областной';
Philharmonic_3 -> 'филармония';
Attractions -> Philharmonic_1<gnc-agr[1]> Philharmonic_2<gnc-agr[1]> Philharmonic_3<gnc-agr[1], rt>;
//Музей-панорама "Сталинградская битва"
Panorama_Museum_1 -> 'музей-панорама';
Panorama_Museum_2 -> AnyWord<wff=/Сталинградская/>;
Panorama_Museum_3 -> 'битва';
Attractions -> Panorama_Museum_1 Panorama_Museum_2 Panorama_Museum_3;
//Мемориально-исторический музей
MH_Museum_1 -> 'мемориально-исторический';
MH_Museum_2 -> 'музей';
Attractions -> MH_Museum_1<gnc-agr[1]> MH_Museum_2<gnc-agr[1], rt>;
//Горсад
Gorsad -> 'горсад';
Attractions -> Gorsad;
//Волгоград Арена
Vlg_Arena_1 -> 'волгоград';
Vlg_Arena_2 -> 'арена';
Attractions -> Vlg_Arena_1<h-reg1> Vlg_Arena_2<h-reg1, rt>;

Attractions_Full -> Attractions interp (Fact.Attractions);


