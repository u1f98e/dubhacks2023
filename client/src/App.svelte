<script>
	import Home from "./home.svelte";
	import About from "./about.svelte";
	import Navbar from "./navbar.svelte";
	import Footer from "./Footer.svelte";

</script>

<style>
	main {
		text-align: left;
		padding: 1em;
		max-width: 240px;
		margin: 0;
		padding: 0;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

<main>
	<Navbar />
	<!-- Pages load here -->

	<!-- <img src="../../cupOWater.jpg" alt="cupOWater"/>; -->
	<Footer />	
</main>



