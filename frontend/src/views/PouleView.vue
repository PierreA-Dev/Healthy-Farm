<template>
<HeaderComponent />
<table>
  <thead class='tableHead'>
    <tr>
      <th>ID</th>
      <th>Température</th>
      <th>Fréquence cardiaque</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="poule in poules" :key="poule.id" v-bind:class="[ poule.is_sick ? 'isSick' : 'isHappy']">
      <td>{{poule.id_animal.id}}</td>
      <td>{{poule.temperature}}</td>
      <td>{{poule.heart_rate}}</td>
      <td><router-link to='/infopoule/{{poule.id_animal.id}}'>Voir plus</router-link></td>
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
  },
}

</script>

<style scoped>
.isSick{
  background-color: red;
}
.isHappy{
  border-top: solid black

}
.tableHead{

}

.tableBody{
  
}

</style>