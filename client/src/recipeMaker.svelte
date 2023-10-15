<script>
	function onSubmit(e) {
		const formData = new FormData(e.target);
		const data = {}
		for (let [key, value] of formData.entries()) {
			if(key == "ingredients") {
				data[key] = value.split(",")
					.map((ingredient) => ingredient.trim());
			} else {
				data[key] = value;
			}
		}

		data["user_id"] = 0;

		fetch("/api/recipe", {
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
	<label for="name">Recipe Name</label>
	<input type="text" id="name" name="name" value=""/>

	<label for="description">Recipe Description</label>
	<input type="text" id="description" name="description" value=""/>

	<label for="instructions">Recipe Instructions</label>
	<input type="text" id="instructions" name="instructions" value=""/>

	<label for="ingredients">Recipe Ingredients</label>
	<input type="text" id="ingredients" name="ingredients" value=""/>

	<label for="image_url">Recipe Image URL</label>
	<input type="text" id="image_url" name="image_url" value=""/>

	<button type="submit">Submit</button>
</form>
