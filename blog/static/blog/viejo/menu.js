var menu = {
    'anido' : {
        'nombre' : 'A-Nido',
        'items' : {
            'integrantes' : {'ref' : 'integrantes.html', 'nombre' : 'Integrantes'},
            'proyecto' : {'ref' : 'proyecto.html', 'nombre' : 'El proyecto'},
            'contribuir' : {'ref' : 'contribuir.html', 'nombre' : 'Contribuir'}
        }
    },
    'articulos' : {
        'nombre' : 'Artículos',
        'items' : {
            'cam19' : {'ref' : 'cam2019.html', 'nombre' : 'Análisis CAM 2019'},
            'craig' : {'ref' : 'entrevista_craig.html', 'nombre' : 'Entrevista a Craig Quat'}
        }
    }
}


var nav = document.querySelector("#nav");
for (var m in menu){
    
    var menu_btn = document.createElement('div');
    menu_btn.setAttribute('id','menu_' + m);
    menu_btn.classList.add('nav_btn');
    
    var link = document.createElement('a');
    link.classList.add('nav_link');
    link.setAttribute('href', '#');
    link.innerText = menu[m]['nombre'];
    
    menu_btn.appendChild(link);
    nav.appendChild(menu_btn);
    
    var items = menu[m]['items'];
    var sub_menu = '<div class="sub_nav">'
    for (var sm in items){
        sub_menu += '<div class="sub_nav_btn"><a class="nav_link" href="' + items[sm]['ref'] + '">' + items[sm]['nombre'] + '</a></div>'
    }
    sub_menu += '</div>'
    
    tippy(menu_btn, {
          allowHTML: true,
          content: sub_menu,
          offset: [0, 0],
          theme: 'menu',
          arrow: false,
          interactive: true,
          placement: 'bottom',
          animation: 'shift-away-subtle'
          });
    /*hideOnClick: false,
     trigger: 'click'*/
}
