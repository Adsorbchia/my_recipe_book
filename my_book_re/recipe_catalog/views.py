from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Cooking at home - все рецепты ',
        'goods': [
    {
        "image": "deps/images/goods/scrambled_eggs.jpg",
        "name": "яичница болтунья",
        "post": " Подготовьте все продукты. Яйца вбейте в миску. Добавьте щепотку соли. Можно поперчить по вкусу. Так блюдо получится более ярким на вкус. С помощью вилки смешайте до однородности желток и белок.",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Omelet_with_avocado.jpg",
        "name": "Омлет с авакадо",
        "post": "Подготовить необходимый набор ингредиентов: яйца, авокадо, соль, чёрный перец, свежую зелень и растительное масло для обжаривания. Очистить половинки авокадо от кожуры. Мякоть нарезать тонкими ломтиками.На сковороде разогреть растительное масло, выложить ломтики авокадо и обжарить с двух сторон по 20-30 секунд. Яйца взболтать венчиком.При желании добавить ко взбитым яйцам немного молока или сливок.Влить на сковороду яичную массу. С помощью лопатки отделить прихватившиеся края омлета от сковороды.Жарить на среднем огне под крышкой в течение 2-3 минут В конце посолить, поперчить и посыпать мелко нарезанной зеленью. Выключить нагрев и оставить омлет под крышкой ещё на 30 секунд. Подавать со свежим хлебом, тостами, чаем или кофе. Приятного аппетита!",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Millet_porridge_with_coconut_milk.jpg",
        "name": "Пшённая каша на кокосовом молоке",
        "post": "Подготовьте необходимые ингредиенты:крупа пшенная, кокосовое молоко, мёд.Пшено пересыпьте в глубокую миску и хорошо промойте.Выложите крупу в сотейник.Влейте в сотейник воду и кокосовое молоко. Перемешайте.Отправьте сотейник на умеренный огонь.Всыпьте соль и ванильный сахар. Перемешайте.После закипания сделайте самый маленький огонь и готовьте пшено, периодически помешивая, 25-35 минут.По вкусу добавьте мёд. Перемешайте.Отключите огонь, накройте сотейник крышкой и оставьте кашу на 8-10 минут.Пшённая каша на кокосовом молоке готова — сразу подавайте к столу. По желанию можно посыпать кокосовой стружкой.Приятного аппетита! ",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/foto3-2484-7.jpg",
        "name": "омлет с курицей и брокколи",
        "post": "Брокколи кладем в кипящую подсоленную воду и варим до готовности (до мягко-хрустящего состояния). Откидываем на дуршлаг, и обязательно под струю холодной воды кладем сваренные соцветия.Куриную грудку режем небольшими кусочками. В сковороде разогреваем смесь масел, кладем грудку, солим, перчим и жарим до белесого цвета. Важно не передержать, чтобы грудка сохранила сочность. Затем добавляем брокколи и мелко нарубленный  чеснок и, помешивая, готовим еще 1 минуту. Тем временем взбиваем яйца со сливками и специями до воздушного однородного состояния. В сковороду добавляем яичную смесь, разравниваем лопаткой, чтобы начинка равномернее распределилась в будущем омлете. Готовим 2-3 минуты, пока низ омлета не зарумянится.Далее – 2 варианта: с помощью тарелки переворачиваем на другую сторону, или ставим в духовку, предварительно разогретую до 200 градусов, и держим до полного схватывания верхушки омлета. Если у вас сковородка большого размера – омлет сверху может приготовиться и без его переворачивания. Приятного аппетита!",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Cheesecakes.jpg",
        "name": "Сырники с кукурузной мукой",
        "post": "Творог выложить в глубокую миску, разбить яйцо и добавить к творогу. Всыпать сахар и растереть творог с сахаром и яйцом при помощи лопатки или столовой ложки в однородную пасту. Добавить в получившуюся массу цедру лимона, снова тщательно растереть с творогом. Влить чайную ложку миндального экстракта и все перемешать.Добавить молотую корицу и две столовые ложки кукурузной муки грубого помола. Тщательно перемешать массу — тесто должно получиться довольно плотным и нелипким.Сформировать из теста аккуратные круглые сырники. В тарелку или миску насыпать немного кукурузной муки и обвалять в ней каждый сырник. Излишки муки стряхнуть обратно в миску.На широкой сковороде разогреть растительное масло и обжарить на нем сырники с обеих сторон до появления румяной корочки. Переложить готовые сырники на блюдо.Украсить каждую порцию листочками свежей мяты и немедленно подавать на стол, пока сырники еще теплые.К сырникам можно добавить джем или же просто перетереть свежую или замороженную клюкву с сахарной пудрой или медом.",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Low-calorie_cottage_cheese_pie.jpg",
        "name": "Творожный низкокалорийный пирог",
        "post": "Муку, разрыхлитель, 0,5 стакана сахара перемешать и добавить нарезанный тонкими кусочками масло. Все ингредиенты перемешать руками — должна получиться мучная крошка — это и есть тесто.Творог размять вилкой, добавить сметану и яичные желтки.Белки взбить с оставшимся сахаром до увеличения в объеме примерно в 3 раза, после чего смешать с творожной массой.В форму для выпечки насыпать две трети теста. Сверху выложить творожно-белковую массу и посыпать оставшимся тестом.Выпекать пирог в разогретой до 180–200 градусов духовке 25–30 минут. Потом духовку выключить, пирог охладить в приоткрытой духовке, затем при комнатной температуре дать ему опуститься. После этого поставить охлаждаться в холодильник. Там он станет плотным, как чизкейк и по вкусу будет его напоминать.",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Buckwheat_soup.jpg",
        "name": "Гречневый суп с курицей и овощами",
        "post": "Отварить куриную грудку. Пока она варится, необходимо хорошо промыть гречку. Порезанный лук с нашинкованной соломкой морковью обжарить на сковороде. Картошку порезать соломкой, как и морковь.В куриный бульон добавить гречку и варить ее до полуготовности около 15 минут, затем добавить поджарку, а через 10 минут — картошку и порезанные помидоры. Как только картофель будет готов, суп можно есть.",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Salad_with_tuna.jpg",
        "name": "Салат с тунцом и фасолью по-тоскански",
        "post": "В миске смешать кусочки тунца, фасоль, разрезанные на четвертинки черри, нарезанный зеленый лук, оливковое масло, лимонный сок и соль.Слегка поперчить по вкусу.Перемешать.Перед подачей охладить.",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Spaghetti.jpg",
        "name": "Спагетти с морепродуктами и помидорами черри",
        "post": "Поставить воду для спагетти.Зубчик чеснока разрезать пополам. Каждый томат аналогично — разрезать на 2 половинки. Подогреть масло в сковороде и бросить чеснок. Дать маслу впитать его вкус, добавить помидоры. Еще некоторое время потомить на медленном огне, пока помидоры не станут нежно-вялыми. Выловить чеснок.Тем временем бросить спагетти в кипяток и довести до состояния аль денте.К помидорам добавить морепродукты. Если прессервы в масле — то дать ему стечь, иначе рыбное масло забьет своим запахом оливковое. Не накрывая крышкой, дать массе подсушиться на сильном огне, Но не пересушить. У осьминогов должны быть золотистая корочка.Выловить специальным половником с отверстием пасту из кастрюли и добавить к соусу с морепродуктами. Влить вино. Дать прокипеть. Посыпать сухим базиликом.",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Mushroom_soup-puree.jpg",
        "name": "Грибной суп-пюре",
        "post": "Порубить лук на мелкие кусочки. Подготовить грибы. Пропустить грибы через мясорубку. Затем добавить в них лук.Смесь обжарить на сковороде с добавлением сливочного масла до испарения воды. Посолить и поперчить по вкусу.Переложить жареные грибы в кастрюлю, залить сливками и довести до кипения. Суп готов.Блюдо можно подавать к столу как в горячем, так и в холодном виде. В последнем случае оно может заменить закуску вроде жюльена.",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Pizza.jpg",
        "name": "Пицца на тесте из куриного филе с помидорами и консервированными грибами",
        "post": "Размельчаем в блендере 500 г сырой куриной грудки и 1 яйцо. Выкладываем ровным слоем «тесто» в форму (лучше на дно положить бумагу для выпекания).Ставим в духовку на 10-15, чтобы корж слегка запекся.Томатной пастой мажем корж из курицы, выкладываем начинку слоями: лук нарезанный полукольцами, помидоры нарезанные полукольцами, грибы, сыр натертый на терке.Добавляем все необходимые приправы (у меня это сушеный укроп, сушеная петрушка, немного соли, прованские травы).Выпекаем при 180 градусах 15 минут.",
        "author": "id_author",
    },
    {
        "image": "deps/images/goods/Lasagna.jpg",
        "name": "Лазанья по-московски",
        "post": "600 гр. сыра нарезать тонкими пластинами 2-3 мм, оставшуюся часть — натереть на крупной терке.Томаты нарезать на тонкие кружочки.Лук обжарить на растительном масле до золотистого цвета.Смешать лук с фаршем, обжарить до готовности.К начинке добавить 4 столовые ложки томатной пасты и полстакана воды. Тушить 10 минут на среднем огне. Посолить, поперчитьВ квадратную не большую форму выложить слой сыра, на него слой начинки. Повторить слои по необходимости. Последним слоем выложить тертый сыр и кружочки томатов.Запекать в разогретой до 200 градусов духовке 10-15 минут.Подавать на стол в форме, украсив зеленью.",
        "author": "id_author",
    },]
    }
    return render(request, 'recipe_catalog/catalog.html', context)

def recipe(request):
    return render()
