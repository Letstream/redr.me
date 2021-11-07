var app = new Vue({
    ...common_vue_config,
    data: {
        newcode: null
    },
    mounted() {
        hide_preloader()
    },
    methods: {
        updateCode(){

            let token = document.getElementById("_token").textContent
            let payload = {
              "code": this.newcode
            }
      
            send_request({
              method: 'PUT',
              url: apiendpoints.edit+token+"/",
              data: payload
            }).then(
              (res) => {
                document.getElementById("_code").innerHTML = this.newcode
                this.newcode = null
                this.$bvToast.toast('URL Edited Succesfully!', {
                    title: 'Success',
                    ...common_toast_options,
                })
              },
              (err) => {
                let response = err.response
                if(response.status == 400) {
                  this.api_errors = response.data.error
                  this.$bvToast.toast(response.data.code[0], {
                    ...common_toast_options,
                    title: 'Error',
                    variant: 'danger'
                  })
                } else {
                  this.$bvToast.toast('An Unknown Error Occurred. Please Try Again!', {
                    ...common_toast_options,
                    title: 'Error',
                    variant: 'danger'
                  })
                }
              }
            )
          }
    }
})