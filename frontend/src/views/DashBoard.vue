<template>
	<HeaderComponent />
	<div class="container">
		<div id="pinrow" class="row">
			<div id='goUp' class="col text-start">
				<h1 class="title">Dashboard</h1>
			</div>
		</div>
		<div class="row">
			<CarouselComponent />
		</div>
		<div class="row">
			<div class='col'>
				<p>Meteo widget</p>
			</div>
		</div>
		<div class="row">
			<div class='col'>
				<p>MAp widget</p>
			</div>
		</div>
		<div class="row">
			<div class='col'>
				<p>histogramme</p>
			</div>
		</div>
	</div>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
import CarouselComponent from "@/components/CarouselComponent";
import axios from 'axios';

export default {
	components: { HeaderComponent, CarouselComponent },
	name: "DashBoard",
	created(){

	},
	methods: {
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
	}
}
</script>

<style scoped>
.title {
	color: black;
	font-family: "Source Sans Pro", sans-serif;
	font-size: 200%;
	font-weight: 600;
}
.hidden {
	display: none;
}
</style>
