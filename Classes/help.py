from rich.console import Console
from rich.table import Table

class Help:
    def __init__(self, arr) -> None:
        self.table_moves = arr

    def generate_table(self):
        table = Table(title='[bold magenta]Turn examples')

        
        columns = ['[bold blue]PC\\USER'] + [f'[bold blue]{move["value"]}' for move in self.table_moves]
        table.add_column(columns[0])
        for move in self.table_moves:
            table.add_column(f'[bold blue]{move["value"]}')

        
        draw_index = len(self.table_moves) // 2

        
        for i, move in enumerate(self.table_moves):
            row = [f'[bold blue]{move["value"]}']  

            
            for j in range(len(self.table_moves)):
                result = ""
                diff = j - i
                if diff == 0:
                    result = "Draw"
                elif diff % len(self.table_moves) in range(1, draw_index + 1):
                    result = "[bold green]Win"
                else:
                    result = "[bold red]loose"
                row.append(result)
            table.add_row(*row)

        console = Console()
        console.print(table)
















