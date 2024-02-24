console.log("js file")
document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
});

document.addEventListener('keydown', function (e) {
    if (((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'I') || 
    ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'C') || 
    ((e.ctrlKey || e.metaKey) && e.altKey && e.key === 'C') || 
    ((e.ctrlKey || e.metaKey) && e.altKey && e.key === 'I')) {
        e.preventDefault();
    }
});

document.addEventListener('keydown', function (e) {
    if ((e.key === 'F12')) {
        e.preventDefault();
    }
});