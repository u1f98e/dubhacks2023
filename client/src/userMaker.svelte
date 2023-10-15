<script>
	function onSubmit(e) {
		const formData = new FormData(e.target);
		const data = {};
		for (let [key, value] of formData.entries()) {
			data[key] = value;
		}

		fetch("/api/user", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data),
		})
			.then((res) => res.json())
			.then((json) => {
				console.log(json);
			});
	}
</script>

<form on:submit|preventDefault={onSubmit}>
	<label for="name">Your Name</label>
	<input type="text" id="name" name="name" value=""/>

	<label for="description">Biography</label>
	<input type="text" id="bio" name="bio" value=""/>

	<label for="instructions">Profile Image</label>
	<input type="text" id="image_url" name="image_url" value=""/>

	<button type="submit">Submit</button>
</form>
