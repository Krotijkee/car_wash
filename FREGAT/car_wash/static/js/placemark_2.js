ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [56.468523, 84.938306],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),

    // Создаем геообъект с типом геометрии "Точка".
        myGeoObject = new ymaps.GeoObject({
            // Описание геометрии.
            geometry: {
                type: "Point",
                coordinates: [56.468523, 84.938306]
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
        myPieChart = new ymaps.Placemark([56.468523, 84.938306], {
            balloonContent: 'цвет <strong>голубой</strong>'
        }, {
            preset: 'islands#blueCircleDotIconWithCaption',
            iconCaptionMaxWidth: '25'
        });

    myMap.geoObjects
        .add(myGeoObject)
        .add(myPieChart)

}
