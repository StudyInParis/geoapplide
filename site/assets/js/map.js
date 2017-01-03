    $(document).ready(function() {
        var map;
        map = new GMaps({
          el: '#map',
          lat: 48.866667,
          lng: 2.3488000
        });
        $.ajax({
            type: 'GET',
            url: 'https://raw.githubusercontent.com/StudyInParis/geoapplide/master/xml_formattes_pivot/xml_pivot.xml',
            dataType: 'xml',
            success: function(xml) {
                // $(xml).find('arrondissement').each(function() {
                //   $(this).find('element').each(function() {
                //     console.log($(this).attr('type'));
                  // alert($(this).attr('type'));
                  // element
                  // alert(element.find('latitude').text());
                  // map.addMarker({
                    // lat: $(this).find('latitude').text(),
                    // lng: $(this).find('longitude').text(),
                    // title: $(this).attr("type"),
                    // icon: '../gmaps/Google Maps Markers/brown_markerA.png',
                    // infoWindow: {
                    //   content: '<p>'+$(this).find('nom').text()+'</br>'+$(this).find('adresse').text()+'</p>'
                    // }
        //             lat: 48.861661,
        // lng: 2.347857,
        // title: 'Marker with InfoWindow',
        // infoWindow: {
        //   content: '<p>HTML Content</p>'
        // }
                //   });
                // });
                // });
            }
        });
    });