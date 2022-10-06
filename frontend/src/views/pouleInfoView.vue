<template>
<HeaderComponent />
<div class='container' style='margin-top:5%'>
  <div class='row'>
    <div class='col-4'>
      <img src='@/assets/toleft.png' @click='$router.push("/poules")'>
    </div>
    <div class='col-4'>
    N° {{pouleId}}
    </div>
    <div class='col-4'>
      <div class="card" :class="pouleData.is_sick ? 'cardSick' : 'cardHealthy'" style="width: 10rem">
        <div class="card-header">
          <div v-show='pouleData.is_sick'>malade</div>
          <div v-show='!pouleData.is_sick'>Saine</div>
        </div>
      </div>    
    </div>
  </div>

  <div class='row' style='margin-top:2em;'>
    <div class='col-4'>
      <img src='@/assets/heart-rate.png'>
    </div>
    <div class='col'>
      <div class='row text-regular'>
        rythme cardiaque
      </div>
      <div class='row'>
        <div class='col text-light'>
        Actuel : {{pouleData.heart_rate}}
        </div>
        <div class='col text-light'>
        Moy: {{pouleData.heart_rate_moy}}
        </div>
      </div>
    </div>
  </div>

  <div class='row' style='margin-top:2em;'>
    <div class='col-4'>
      <img src='@/assets/temperature.png'>
    </div>
    <div class='col'>
      <div class='row text-regular'>
        Température
      </div>
      <div class='row'>
        <div class='col text-light'>
        Actuel : {{pouleData.temperature}}
        </div>
        <div class='col text-light'>
        Moy: {{pouleData.temperature_moy}}
        </div>
      </div>
    </div>
  </div>

  <div class='row' style='margin-top:2em;'>
    <p class='title'>Localisation</p>
    <div>img</div>
  </div>

  <div class='row' style='margin-top:2em;'>
    <p class='title'>Historique</p>
    <div>histogramme</div>
  </div>
</div>
{{pouleData}}

  
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import axios from "axios";
export default {
 components: { HeaderComponent },
  name:'pouleInfoView',
  data(){
    return {
      pouleData: {}
    }
  },
  created() {
    this.getPoule();
  },
  props: ['pouleId', 'data'],
  methods: {
  async getPoule () {
      try{
        const res = await axios.get("http://127.0.0.1:5000/mon_animal", {
            headers: {
              "Access-Control-Allow-Origin": "*",
            },
            params: {
              "id": this.pouleId,
            }
          })
        this.pouleData = res.data[0] 
      } catch (error){
        console.log(error);
      }
    },
  }

}
</script>

<style scoped>
  .cardHealthy{
    max-width: 90% ;
    background-color: #44CF6C;
  }
  .cardSick{
    max-width: 90% ;
    background-color: #FF473E;
  }

  .title{
    color: #32A287;
    font-family:'Source Sans Pro', sans-serif;
    font-weight:600;
  }

</style>