function rechazar(id) {
    Swal.fire({
        title: 'Rechazar',
        text: "Esta seguro de rechazar esta noticia",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si,Rechazar'
      }).then((result) => {
        if (result.isConfirmed) {
          location.href='rechazar_not/'+id+'/';
        }
      }) 
}