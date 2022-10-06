<template>
<HeaderComponent />
<table style='margin-top:5%'>
  <thead class='tableHead'>
    <tr>
      <th class='colone1'>ID</th>
      <th class='colone'>Température</th>
      <th class='colone'>Fréquence cardiaque</th>
      <th class='colone'></th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="poule in poules" :key="poule.id" v-bind:class="[ poule.is_sick ? 'isSick' : 'isHappy']">
      <td>{{poule.id_animal.id}}</td>
      <td>{{poule.temperature}}</td>
      <td>{{poule.heart_rate}}</td>
      <td><button @click='gotoInfoPoule(poule.id_animal.id)'>Voir plus</button></td>
    </tr>
  </tbody>
</table>
<ul>
</ul>
  
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import axios from "axios";

export default {
  components: { HeaderComponent },
  name:'PouleView',
  data() {
		return {
			poules: "",
		};
	},
  created() {
    this.getPoules();
  },
  methods:{
    async getPoules () {
      try{
        const res = await axios.get("http://127.0.0.1:5000/liste_des_animaux", {
            headers: {
              "Access-Control-Allow-Origin": "*",
            },
          })
        this.poules = res.data   
      } catch (error){
        console.log(error);
      }
    },
    gotoInfoPoule(id) {
      this.$router.push('/infopoule/'+ id)
    }
  },
}

</script>

<style scoped>
.isSick{
  background-color: red;
}
.isHappy{
  border-top: 1px solid black;
  margin: 10%;

}
.colone1{
  padding-inline: 20px;
}
.colone{
  padding-inline: 7px;
  padding: 7px;
}

.tableHead{
  font-size: 0.9em;
}

button{
  border-radius:12px;
  min-width:123%;
  margin-left: -25%;
}


</style>