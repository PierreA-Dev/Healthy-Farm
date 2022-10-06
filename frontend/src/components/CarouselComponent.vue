<template>
<div
    id="carouselExampleControls"
    class="carousel slide"
    data-bs-ride="false"
    data-interval="false"
  >
    <div class="carousel-inner">
      <div class="carousel-item active">
        <div class="row">
          <div class="col" style='margin-left: 1em;'>
            <div class="card" style="width: 10rem">
              <div class="card-header">Featured1</div>
            </div>
          </div>
          <div class="col" style='margin-right: 1.5em;'>
            <div class="card" style="width: 10rem">
              <div class="card-header">Featured2</div>
            </div>
          </div>
        </div>
      </div>
      <div class="carousel-item">
        <div class="row">
          <div class="col" style='margin-left: 2.5em;'>
            <div class="card" style="width: 10rem">
              <div class="card-header">Featured3</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <button
      v-show="carouselPage == 2"
      @click='carouselPage = 1'
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleControls"
      data-bs-slide="prev"
    >
      <img src='@/assets/toleft.png'>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      v-show="carouselPage == 1"
      @click='carouselPage = 2'
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleControls"
      data-bs-slide="next"
    >
      <img src='@/assets/toright.png'>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  
</template>

<script>
export default {
  name:'CarouselComponent',
  data(){
    return {
      carouselPage: 1
    }
  },
}
</script>

<style scoped>
.card-header {
	height: 10em;
}
.card{
  border-radius: 15px;
  box-shadow: 2em;
}
</style>