# fog_testing_todo
Fog.
- [x] As a user my todos should be saved in a file so they persist when the program is not running
- [ ] As a user I should be able to view my todos by typing something like `view`
- [ ] As a user I should be able to add simple todos by typing something like `add "buy coffee creamer"`
- [ ] As a user I should be able to mark todos as completed by typing something like `done 1`
- [ ] As a user I should be able to unmark todos as completed by typing something like `undo 1`
- [ ] As a user I should be able to delete todos by typing something like `delete 1`

When I view my todos I should see something like this:
```
1: buy coffee creamer
2: make list of todos
3: finish todo app
```

## Schema
a todo is:
id = a number that refers to that todo easily
todo_text = "buy coffee creamer"
done = done / not done