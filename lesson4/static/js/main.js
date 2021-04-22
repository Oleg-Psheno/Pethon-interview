$.get( "/ajax_handler", function( data ) {
  let out = ``

  let dat = JSON.parse(data);
  let d = JSON.parse(data)[0].fields.name;
  dat.forEach(function (item){

    out += `<div class="item col-4">
            <p>Наименование товара - ${item.fields.name}</p>
            <p>Остаток на складе  - ${item.fields.quantity}</p>
            <p>${item.fields.description}</p>
               <br>
           </div>`
  });
      $( "#test" ).html( out );
    }

);

