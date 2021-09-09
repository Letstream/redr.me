var common_vue_config = {
    el: "#app",
    delimiters: ['[[', ']]'], // Override Conflicting Delimiters because of DTL
}

var common_toast_options = {
    autoHideDelay: 5000,
    appendToast: false,
    variant: 'success',
    toaster: 'b-toaster-bottom-center'
}

function hide_preloader(){
    document.getElementById("preloader").style.top = "-120vh"
    setTimeout(() => {
        document.getElementById("preloader").style.display = "none"
    }, 2000)
}

function copy_text(id, vue_instance=null) {
    const copyText = document.getElementById(id);
  
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
    /* Copy the text inside the text field */
    document.execCommand("copy");

    if(vue_instance) {
        vue_instance.$bvToast.toast('URL Copied Succesfully!', {
            title: 'Success',
            ...common_toast_options,
        })
    }
}

function copy_arbitary_text(value, vue_instance=null) {
    // Insert a temporary field in DOM
    const copyText = document.createElement("input")
    let id = "temp-" + Date.now()
    copyText.id = id
    copyText.value = value
    copyText.style.opacity = 0
    document.getElementsByTagName("body")[0].append(copyText)

    /* Select the text field */
    let inserted_field = document.getElementById(id)
    inserted_field.select();
    inserted_field.setSelectionRange(0, 99999); /* For mobile devices */
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
    
    // Remove the temporary field from DOM
    inserted_field.remove()

    if(vue_instance) {
        vue_instance.$bvToast.toast('URL Copied Succesfully!', {
            title: 'Success',
            ...common_toast_options,
        })
    }
}

function send_request({
    url=null,
    method=null,
    data=null,
    params=null,
    headers=null,
    with_credentials=true,
    vue_instance=null
}={}) {

    return new Promise((resolve, reject) => {

        if(!headers)
            headers = {}
        
        headers['X-CSRFToken'] = Cookies.get('csrftoken');

        axios({
            method: method,
            url: url,
            data: data,
            params: params,
            headers: headers,
            withCredentials: with_credentials
          }).then(
            (res) => {
                resolve(res.data)
            },
            (err) => {
                if(!err.response) {
                    if(vue_instance) {
                        vue_instance.$bvToast.toast('A Network Error Occurred. Please check your internet connection and try Again.', {
                            ...common_toast_options,
                            title: 'Network Error',
                            variant: 'danger'
                        })
                    }
                    reject(err)
                } else {
                    let response = err.response
                    if(response.status == 400 && vue_instance) {
                        vue_instance.$bvToast.toast('Please fix the errors and try again', {
                            ...common_toast_options,
                            title: 'Error',
                            variant: 'danger'
                        })
                    }
                    reject(err)
                }
            }
        )
    })
}