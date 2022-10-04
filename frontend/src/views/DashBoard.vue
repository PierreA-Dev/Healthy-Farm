<template>
	<HeaderComponent/>
	<div class="container">
		<div class='row'>
			<div class='col text-start'>
				<h1 class='title'>Dashboard</h1>
			</div>
		</div>
		<div class='row'>
			<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
				<div class="carousel-inner">
					<div class="carousel-item active">
						<img src="" class="d-block w-100" alt="...">
					</div>
					<div class="carousel-item">
						<img src="" class="d-block w-100" alt="...">
					</div>
					<div class="carousel-item">
						<img src="" class="d-block w-100" alt="...">
					</div>
				</div>
				<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
					<span class="carousel-control-prev-icon" aria-hidden="true"></span>
					<span class="visually-hidden">Previous</span>
				</button>
				<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
					<span class="carousel-control-next-icon" aria-hidden="true"></span>
					<span class="visually-hidden">Next</span>
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent';

export default {
	components: {HeaderComponent },
	name: "DashBoard",
};
</script>

<style scoped>

.title {
    color: black;
    font-family:'Source Sans Pro', sans-serif;
    font-size: 200%;
    font-weight:600;
  }

</style>
