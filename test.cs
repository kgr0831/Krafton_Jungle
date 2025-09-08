namespace homework
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<string> name = new List<string>();
            List<int> score = new List<int>();

            Console.WriteLine("학생 수");
            int student = int.Parse(Console.ReadLine());

            for (int i = 0; i < student; i++)
            {
                Console.WriteLine("이름");
                string _name = Console.ReadLine();

                name.Add(_name);

                Console.WriteLine("점수");
                int _score = int.Parse(Console.ReadLine());

                if (_score < 0) score.Add(0);
                else if (_score > 100) score.Add(100);
                else score.Add(_score);

                Console.WriteLine($"이름 {name[i]} , 점수 {score[i]}");
                Console.ReadLine();
                Console.Clear();
            }

            int high = score[0];
            string high_name = name[0];
            int low = score[0];
            string low_name = name[0];
            float average_score = 0;

            for (int j = 1; j < student; j++)
            {
                if (high <= score[j])
                {
                    high = score[j];
                    high_name = name[j];
                }
                if (low >= score[j])
                {
                    low = score[j];
                    low_name = name[j];
                }
            }

            foreach (int s in score)
            {
                average_score += s;
            }
            average_score /= student;

            Console.WriteLine($"최고 점수 : {high}점 ({high_name})");
            Console.WriteLine($"최저 점수 : {low}점 ({low_name})");
            Console.WriteLine($"평균 점수 : {average_score}점");
        }

    }
}