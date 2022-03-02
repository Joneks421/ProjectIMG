function scroller_about(element){
    window.scroll({
        left: 0,
        top: element.offsetTop,
        behavior: 'smooth'
    })
    

}
var button = document.querySelector('.button');
var footer = document.querySelector('#footer')
