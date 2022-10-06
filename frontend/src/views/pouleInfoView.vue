<template>
<HeaderComponent />
<div class='container'>
  <div class='row'>
    <div class='col'>
    fleche
    </div>
    <div class='col'>
    N° {{pouleId}}
    </div>
    <div class='col'>
      malade
    </div>
  </div>

  <div class='row'>
    <div class='col'>
      imgcoeur
    </div>
    <div class='col'>
      <div class='row'>
        rythme cardiaque
      </div>
      <div class='row'>
        <div class='col'>
        Actuel : *
        </div>
        <div class='col'>
        Moy: *
        </div>
      </div>
    </div>
  </div>

  <div class='row'>
    <div class='col'>
      imgthermometre
    </div>
    <div class='col'>
      <div class='row'>
        Température
      </div>
      <div class='row'>
        <div class='col'>
        Actuel : *
        </div>
        <div class='col'>
        Moy: *
        </div>
      </div>
    </div>
  </div>

  <div class='row'>
    Localisation
    <div>img</div>
  </div>

  <div class='row'>
    Historique
    <div>histogramme</div>
  </div>
</div>

  
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent";
export default {
 components: { HeaderComponent },
  name:'pouleInfoView',
  props: ['pouleId'],

}
</script>

<style>

</style>