var options = [
  {"name":"Home",
    "url":"{% url 'landing' %}",
  },
  {"name":"Aluno",
  "url":"{% url 'authentication' slug='login' %}",
},
  {"name":"Professor",
  "url":"{% url 'authentication' slug='login' %}",
},
  { "name":"About",
    "url":"{% url 'about' %}",
  },
]

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
