ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [56.482200, 84.984605],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),

    // Создаем геообъект с типом геометрии "Точка".
        myGeoObject = new ymaps.GeoObject({
            // Описание геометрии.
            geometry: {
                type: "Point",
                coordinates: [56.482200, 84.984605]
            },
            // Свойства.
            properties: {
                // Контент метки.
                iconContent: 'Автомойка "Фрегат"'
            }
        }, {
            // Опции.
            // Иконка метки будет растягиваться под размер ее содержимого.
            preset: 'islands#blackStretchyIcon',
            // Метку можно перемещать.
            draggable: false
        }),
        myPieChart = new ymaps.Placemark([56.482200, 84.984605], {
            balloonContent: 'цвет <strong>голубой</strong>'
        }, {
            preset: 'islands#blueCircleDotIconWithCaption',
            iconCaptionMaxWidth: '25'
        });

    myMap.geoObjects
        .add(myGeoObject)
        .add(myPieChart)
        // .add(new ymaps.Placemark([56.482200, 84.984605], {
        //     balloonContent: 'цвет <strong>воды пляжа бонди</strong>'
        // }, {
        //     preset: 'islands#icon',
        //     iconColor: '#0095b6'
        // }))
        // .add(new ymaps.Placemark([56.482200, 84.984605], {
        //     balloonContent: '<strong>серобуромалиновый</strong> цвет'
        // }, {
        //     preset: 'islands#dotIcon',
        //     iconColor: '#735184'
        // }))
        // .add(new ymaps.Placemark([56.482200, 84.984605], {
        //     balloonContent: 'цвет <strong>влюбленной жабы</strong>'
        // }, {
        //     preset: 'islands#circleIcon',
        //     iconColor: '#3caa3c'
        // }))
        // .add(new ymaps.Placemark([56.482200, 84.984605], {
        //     balloonContent: 'цвет <strong>детской неожиданности</strong>'
        // }, {
        //     preset: 'islands#circleDotIcon',
        //     iconColor: 'yellow'
        // }))
        // .add(new ymaps.Placemark([56.482200, 84.984605], {
        //     balloonContent: 'цвет <strong>красный</strong>'
        // }, {
        //     preset: 'islands#redSportIcon'
        // }))
        // .add(new ymaps.Placemark([55.826479, 37.487208], {
        //     balloonContent: 'цвет <strong>фэйсбука</strong>'
        // }, {
        //     preset: 'islands#governmentCircleIcon',
        //     iconColor: '#3b5998'
        // }))
        // .add(new ymaps.Placemark([55.694843, 37.435023], {
        //     balloonContent: 'цвет <strong>носика Гены</strong>',
        //     iconCaption: 'Очень длиннный, но невероятно интересный текст'
        // }, {
        //     preset: 'islands#greenDotIconWithCaption'
        // }))
        // .add(new ymaps.Placemark([55.790139, 37.814052], {
        //     balloonContent: 'цвет <strong>голубой</strong>',
        //     iconCaption: 'Очень длиннный, но невероятно интересный текст'
        // }, {
        //     preset: 'islands#blueCircleDotIconWithCaption',
        //     iconCaptionMaxWidth: '50'
        // }));
}
