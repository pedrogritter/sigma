new Vue({
  delimiters: ['[[', ']]'],
  el: "#slider",

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
