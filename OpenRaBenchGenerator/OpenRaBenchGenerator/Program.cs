using System;
using System.Text;

namespace OpenRaBenchGenerator
{
	class Program
	{
		static void Main(string[] args)
		{
			var random = new Random();

			var stringBuilder = new StringBuilder();

			stringBuilder.Append("spawns = {");
			for (int i = 0; i < 200; i++)
			{
				var x = random.Next(1, 64);
				var y = random.Next(0, 64);
				stringBuilder.Append($"CPos.New({x}, {y}), ");

				//Console.WriteLine($"local a{i} = Actor.Create(\"bggy\", true, {{Location = spawn}} )");

			}

			stringBuilder.Append("}");
			Console.WriteLine(stringBuilder);

			Console.Read();
		}
	}
}
