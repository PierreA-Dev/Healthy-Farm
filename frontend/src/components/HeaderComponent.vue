<template>
	<nav class="navbar sticky-top bg-light">
		<div class="container-fluid">
			<div class="row">
				<div class="col-3">
					<div class="dropdown">
						<button
							class="btn btn-secondary dropdown-toggle menuButton"
							id="dropdownMenuLink"
							data-bs-toggle="dropdown"
							aria-expanded="false"
						>
							<span class="navbar-toggler-icon"></span>
						</button>
						<ul
							class="dropdown-menu"
							aria-labelledby="dropdownMenuLink"
							id="dropdownMenu"
						>
							<li class="nav-item">
								<div class="card specialCard">
									<div class="card-header">
										<router-link to="/poules" class="nav-link active text-regular"
											><img class="icon-menu" src="@/assets/chicken_icon.png" />Liste des poules</router-link
										>
									</div>
								</div>
							</li>
							<li class="nav-item">
								<div class="card specialCard">
									<div class="card-header">
										<router-link to="/" class="nav-link active text-regular"
											><img class="icon-menu" src="@/assets/help.png" />Guides</router-link
										>
									</div>
								</div>
							</li>
							<li class="nav-item">
								<div class="card specialCard">
									<div class="card-header">
										<router-link to="/" class="nav-link active text-regular"
											><img class="icon-menu" src="@/assets/settings.png" />Gestion du compte</router-link
										>
									</div>
								</div>
							</li>
							<li class="nav-item">
								<div class="card specialCard">
									<div class="card-header">
										<router-link to="/" class="nav-link active text-regular"
											><img class="icon-menu" src="@/assets/notif.png" />Préférences de notification</router-link
										>
									</div>
								</div>
							</li>
							<li class="nav-item">
								<div class="card specialCard">
									<div class="card-header">
										<router-link to="/" class="nav-link active text-regular"
											>Déconnexion</router-link
										>
									</div>
								</div>
							</li>
							<div class="dropdown-divider" style="margin-top: 4em;"></div>
							<li>
								<router-link to="/" class="nav-link active otherLinks" style="margin-top: 2em;"
									>Centre d'aide et d'information</router-link
								>
							</li>
							<li>
								<router-link to="/" class="nav-link active otherLinks"
									>Politique de confidentialité</router-link
								>
							</li>
							<li>
								<router-link to="/" class="nav-link active otherLinks"
									>Conditions générales d'utilisation</router-link
								>
							</li>
							<li>
								<p class='otherLinks'>Version: 1.0</p>
							</li>
						</ul>
					</div>
				</div>
				<div class="col-3">
					<img class="icon" src="@/assets/chicken_icon.png" @click='goToDashboard'/>
				</div>
				<div class="col-1">
					<p class="text" @click='goToDashboard'>Healthy'Farm</p>
				</div>
			</div>
			<div class="col-1">
				<img class="icons" src="@/assets/notif.png" />
			</div>
			<div class="col-1">
				<img class="icons" src="@/assets/account.png" />
			</div>
		</div>
	</nav>
</template>

<script>
export default {
	data() {
		return {
			showMenu: false,
		};
	},
  mounted() {
    var body = document.body,
        html = document.documentElement;

    var height = Math.max( body.scrollHeight, body.offsetHeight, 
                       html.clientHeight, html.scrollHeight, html.offsetHeight );
    var dropdownMenu = document.getElementById('dropdownMenu');
    dropdownMenu.style.minHeight = height+"px";

  },
	methods: {
		toggleShowMenu() {
			if (this.showMenu == false) {
				this.showMenu = true;
			} else {
				this.showMenu = false;
			}
		},
		goToDashboard() {
			this.$router.push('/dashboard')
		}
	},
};
</script>

<style scoped>
.navbar {
	box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
	-moz-box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
	-webkit-box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.specialCard{
  max-width: 13em;
  margin-left: 1em;
  margin-bottom: 1em;
  border-radius: 20px !important;
  margin-top: 1em;
}

.menuButton {
	height: 4em;
	background-color: #f8f9fa;
	border: none;
}
.menu {
	position: sticky;
}
.icon {
	max-height: 50px;
	margin-top: 10%;
}
.icon-menu{
  max-height: 30px;
  margin-right: 2%;
}
.icons {
	height: 30px;
	margin-right: 5%;
}
.dropDownButton {
	margin-top: 10%;
	height: 100%;
	width: 200%;
	margin-left: -20%;
	border: none;
}
.text {
	margin-top: 20px;
	margin-left: -10px;
	font-family: "kanit";
  font-size: 0.9em;
  font-weight:600;
}

#dropdownMenu {
	min-width: 600%;
	margin-left: -0.8em;
	margin-top: 0.5em;
}

.text-regular{
  font-size: 0.9em;
  font-family: 'Source Sans Pro', sans-serif;
  font-weight:600;
	color: black;
}

.otherLinks {
  padding:1em;
}

</style>