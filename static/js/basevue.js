new Vue({
  delimiters: ['[[', ']]'],
  el: "#app",

  data: {
    open: false,
    show: false,
    options: options,
  },

  methods: {
    toggleNav: function() {
      this.open = !this.open
      this.$emit('toggle', this.open)
    }
  }
})
