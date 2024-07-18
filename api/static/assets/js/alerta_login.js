
// alerta_login.js
document.addEventListener('DOMContentLoaded', function() {
    if (typeof djangoMessages !== 'undefined' && djangoMessages.length > 0) {
        djangoMessages.forEach(function(item) {
            Swal.fire({
                icon: item.tags === "error" ? "error" : 
                      item.tags === "success" ? "success" : 
                      item.tags === "warning" ? "warning" : "info",
                title: item.message,
                timer: 3000,
                showConfirmButton: false
            });
        });
    }
});
