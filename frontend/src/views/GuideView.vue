<template>
<HeaderComponent />
<div class='container'>
  <div class='row'>
    <div class='col-12' style='margin-top:1em; font-size:1.5em; text-align:left;'>
      <p class='text-regular'>Comment ça fonctionne ?</p>
    </div>
    <div class='col-12' style='text-align:justify; text-justify: auto;'>
      <p class='text-light'>Un bracelet connecté qui permet de récupérer la température et le rythme cardiaque
      de votre poule afin de prévenir d'une éventuelle épidémie.</p>
    </div>
  </div>

  <div class='row' style='margin-top:1em;'>
    <div class='col-12'>
      <img v-show='img === "poule1"' src='@/assets/poule1.png' @click='toggleImg'>
      <img v-show='img === "poule2"' src='@/assets/poule2.png' @click='toggleImg'>
    </div>
  </div>

  <div class='row' style='margin-top:2em;'>
    <div class='col-12'>
      <img v-show='!lux' src='@/assets/collar.png'>
      <img v-show='lux' src='@/assets/collarlux.png'>
    </div>
  </div>
</div>
  
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
export default {
  name:'GuideView',
  components: { HeaderComponent },
  data() {
    return {
      img: 'poule1',
      lux: false,
    }
  },
  mounted() {
    this.setTimer();
    
  },
  methods:{
    toggleImg() {
      switch (this.img) {
        case 'poule1': this.img = 'poule2';
          break;
        case 'poule2': this.img = 'poule1';
          break;
      }
    },
    toggleCollar() {
      this.lux = ! this.lux;
    },
    setTimer() {
      setInterval(this.toggleCollar(), 200);
    }
  },
}
</script>

<style scoped>
 

</style>