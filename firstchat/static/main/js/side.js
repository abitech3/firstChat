

var links = document.querySelectorAll('.sidebar-nav .nav-item .nav-link');
links.forEach( link => {
link.addEventListener('click', ()=> {
 links.forEach(l => l.classList.remove('act'));
var x = link.classList.add('act'); 
console.log(x);

})
})
